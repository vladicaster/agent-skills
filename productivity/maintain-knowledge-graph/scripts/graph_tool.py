#!/usr/bin/env python3
"""Validate and prepare classified graphs. No network or provider writes."""
import argparse
import copy
import hashlib
import json
import os
import re
import sys
import uuid
from pathlib import Path

VIS = {'public', 'private', 'unclassified'}
SCHEMA = 'classified-graph/1'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keys(obj, expected, where):
    require(isinstance(obj, dict) and set(obj) == set(expected), f'{where}: invalid envelope keys')


def identifier(value):
    try:
        parsed = uuid.UUID(value)
        return parsed.version == 4 and str(parsed) == value
    except (ValueError, TypeError, AttributeError):
        return False


def fields(value, where):
    require(isinstance(value, dict), f'{where}: fields must be an object')
    for name, item in value.items():
        require(re.fullmatch(r'[a-z][a-z0-9_]*', name) is not None, f'{where}: invalid field name')
        keys(item, {'visibility', 'value'}, where)
        require(isinstance(item['visibility'], str) and item['visibility'] in VIS, f'{where}: invalid field visibility')
        # Reject non-JSON and nonfinite values even when called through the Python API.
        json.dumps(item['value'], allow_nan=False)


def required_text(record, name):
    item = record['fields'].get(name)
    require(item is not None and isinstance(item['value'], str) and bool(item['value'].strip()), f'record missing nonempty {name}')


def validate(graph):
    keys(graph, {'schema_version', 'graph_id', 'revision', 'fields', 'nodes', 'edges'}, 'graph')
    require(graph['schema_version'] == SCHEMA, 'unsupported schema')
    require(identifier(graph['graph_id']), 'graph_id must be canonical UUID4')
    require(type(graph['revision']) is int and graph['revision'] >= 1, 'revision must be positive integer')
    fields(graph['fields'], 'graph')
    require(isinstance(graph['nodes'], list) and isinstance(graph['edges'], list), 'nodes/edges must be lists')
    seen = {graph['graph_id']}
    node_ids = set()
    for kind in ('nodes', 'edges'):
        for record in graph[kind]:
            expected = {'id', 'visibility', 'fields'} | ({'source', 'target'} if kind == 'edges' else set())
            keys(record, expected, kind)
            require(identifier(record['id']) and record['id'] not in seen, 'invalid or duplicate record UUID')
            seen.add(record['id'])
            require(isinstance(record['visibility'], str) and record['visibility'] in VIS, 'invalid record visibility')
            fields(record['fields'], kind)
            if kind == 'nodes':
                required_text(record, 'label')
                required_text(record, 'type')
                node_ids.add(record['id'])
            else:
                required_text(record, 'relation')
                require(identifier(record['source']) and identifier(record['target']), 'invalid edge endpoints')
                require(record['source'] in node_ids and record['target'] in node_ids, 'dangling edge')
    return graph


def project(graph, audience):
    validate(graph)
    require(audience in {'public', 'private'}, 'invalid audience')
    if audience == 'private':
        return copy.deepcopy(graph)
    result = {key: copy.deepcopy(graph[key]) for key in ('schema_version', 'graph_id')}
    result.update(revision=1, fields=public_fields(graph['fields']), nodes=[], edges=[])
    for node in graph['nodes']:
        visible = public_fields(node['fields'])
        if node['visibility'] == 'public' and {'label', 'type'} <= set(visible):
            result['nodes'].append({'id': node['id'], 'visibility': 'public', 'fields': visible})
    ids = {node['id'] for node in result['nodes']}
    for edge in graph['edges']:
        visible = public_fields(edge['fields'])
        if edge['visibility'] == 'public' and edge['source'] in ids and edge['target'] in ids and 'relation' in visible:
            result['edges'].append({'id': edge['id'], 'visibility': 'public', 'source': edge['source'], 'target': edge['target'], 'fields': visible})
    return validate(result)


def public_fields(items):
    return {key: copy.deepcopy(value) for key, value in items.items() if value['visibility'] == 'public'}


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, 'duplicate JSON key')
        obj[key] = value
    return obj


def load(path):
    return validate(read_json(path))


def read_json(path):
    with open(path, encoding='utf-8') as handle:
        return json.load(handle, object_pairs_hook=unique_object, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON value')))


def migrate(legacy):
    """Convert the earlier property graph conservatively; never infer public consent."""
    require(isinstance(legacy, dict) and legacy.get('format') == 'personal_property_graph', 'unsupported legacy format')
    private = legacy.get('private_context', {})
    require(isinstance(private, dict), 'invalid private context')
    grouped = []
    for context, visibility in ((legacy, 'unclassified'), (private, 'private')):
        nodes, edges = context.get('nodes', []), context.get('edges', [])
        require(isinstance(nodes, list) and isinstance(edges, list), 'invalid legacy records')
        grouped.append((nodes, edges, visibility))
    graph = {'schema_version': SCHEMA, 'graph_id': str(uuid.uuid4()), 'revision': 1, 'fields': {}, 'nodes': [], 'edges': []}
    mapping = {}

    def wrapped(value, visibility):
        return {'visibility': visibility, 'value': copy.deepcopy(value)}

    for nodes, _, visibility in grouped:
        for node in nodes:
            require(isinstance(node, dict), 'invalid legacy node')
            old_id = node.get('id')
            require(isinstance(old_id, str) and bool(old_id) and old_id not in mapping, 'duplicate or invalid legacy node id')
            mapping[old_id] = str(uuid.uuid4())
            graph['nodes'].append({'id': mapping[old_id], 'visibility': visibility, 'fields': {
                'label': wrapped(node.get('label'), visibility),
                'type': wrapped(node.get('type'), visibility),
                'legacy_record': wrapped(node, visibility),
            }})
    edge_ids = {}
    for _, edges, visibility in grouped:
        for edge in edges:
            require(isinstance(edge, dict), 'invalid legacy edge')
            old_id = edge.get('id')
            require(isinstance(old_id, str) and bool(old_id) and old_id not in edge_ids, 'duplicate or invalid legacy edge id')
            source, target = edge.get('source'), edge.get('target')
            require(isinstance(source, str) and isinstance(target, str) and source in mapping and target in mapping, 'dangling legacy edge')
            edge_ids[old_id] = str(uuid.uuid4())
            graph['edges'].append({'id': edge_ids[old_id], 'visibility': visibility, 'source': mapping[source], 'target': mapping[target], 'fields': {
                'relation': wrapped(edge.get('type'), visibility),
                'legacy_record': wrapped(edge, visibility),
            }})
    graph['fields']['legacy_id_map'] = wrapped({'nodes': mapping, 'edges': edge_ids}, 'private')
    graph['fields']['legacy_metadata'] = wrapped({k: v for k, v in legacy.items() if k not in {'nodes', 'edges', 'private_context'}}, 'unclassified')
    graph['fields']['legacy_private_context'] = wrapped({k: v for k, v in private.items() if k not in {'nodes', 'edges'}}, 'private')
    return validate(graph)


def encoded(graph):
    return (json.dumps(graph, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode('utf-8')


def viewer(graph, audience):
    template = (Path(__file__).resolve().parent.parent / 'assets' / 'viewer.html').read_text(encoding='utf-8')
    value = json.dumps(graph, ensure_ascii=False, allow_nan=False).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
    return template.replace('__AUDIENCE__', audience).replace('__GRAPH_DATA__', value).encode('utf-8')


def write_new(path, contents):
    # Exclusive creation prevents accidental replacement of a master or approved candidate.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'wb') as handle:
        handle.write(contents)
    return {'path': str(Path(path).resolve()), 'sha256': hashlib.sha256(contents).hexdigest(), 'bytes': len(contents)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    init = sub.add_parser('init')
    init.add_argument('--output', required=True)
    check = sub.add_parser('validate')
    check.add_argument('input')
    migration = sub.add_parser('migrate')
    migration.add_argument('input')
    migration.add_argument('--output', required=True)
    export = sub.add_parser('export')
    export.add_argument('input')
    export.add_argument('--audience', required=True, choices=['public', 'private'])
    export.add_argument('--output', required=True)
    export.add_argument('--viewer')
    args = parser.parse_args()
    written = []
    try:
        if args.command == 'init':
            graph = {'schema_version': SCHEMA, 'graph_id': str(uuid.uuid4()), 'revision': 1, 'fields': {}, 'nodes': [], 'edges': []}
            written.append(write_new(args.output, encoded(graph)))
        elif args.command == 'validate':
            graph = load(args.input)
            print(json.dumps({'valid': True, 'nodes': len(graph['nodes']), 'edges': len(graph['edges'])}))
            return 0
        elif args.command == 'migrate':
            graph = migrate(read_json(args.input))
            require(Path(args.input).resolve() != Path(args.output).resolve(), 'output cannot replace input')
            written.append(write_new(args.output, encoded(graph)))
        else:
            graph = project(load(args.input), args.audience)
            candidates = [(args.output, encoded(graph))]
            if args.viewer:
                candidates.append((args.viewer, viewer(graph, args.audience)))
            paths = [Path(path).resolve() for path, _ in candidates]
            require(len(set(paths)) == len(paths), 'outputs must be distinct')
            require(Path(args.input).resolve() not in paths, 'output cannot replace input')
            for path in paths:
                require(not path.exists() and not path.is_symlink(), 'output already exists')
                require(path.parent.is_dir(), 'create output directory first')
            for path, contents in candidates:
                written.append(write_new(path, contents))
        print(json.dumps({'prepared_not_published': True, 'files': written}))
        return 0
    except (ValueError, TypeError, OSError, KeyError, RecursionError) as error:
        # Never echo field values, which may be private.
        print(json.dumps({'error': type(error).__name__, 'message': 'Preparation failed; validate schema, inputs and unused output paths.', 'prepared_files': written}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
