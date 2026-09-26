"""Synthetic regression tests for the disclosure boundary."""
import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
import graph_tool as tool


def uid():
    return str(uuid.uuid4())


def field(value, visibility='public'):
    return {'visibility': visibility, 'value': value}


def node(label, visibility='public'):
    return {'id': uid(), 'visibility': visibility, 'fields': {'label': field(label), 'type': field('Person')}}


class DisclosureTests(unittest.TestCase):
    def setUp(self):
        self.a = node('Synthetic subject')
        self.b = node('PRIVATE_ENTITY_CANARY', 'private')
        self.c = node('Public project')
        self.a['fields'].update(salary=field('PRIVATE_FIELD_CANARY', 'private'), claim=field('UNCLASSIFIED_CANARY', 'unclassified'), evidence=field({'url': 'PRIVATE_URL_CANARY'}, 'private'))
        self.graph = {'schema_version': tool.SCHEMA, 'graph_id': uid(), 'revision': 17, 'fields': {'notes': field('PRIVATE_METADATA_CANARY', 'private')}, 'nodes': [self.a, self.b, self.c], 'edges': []}
        for target in (self.b, self.c):
            self.graph['edges'].append({'id': uid(), 'visibility': 'public', 'source': self.a['id'], 'target': target['id'], 'fields': {'relation': field('CONNECTED_TO'), 'notes': field('PRIVATE_EDGE_CANARY', 'private')}})

    def test_public_json_and_html_exclude_private(self):
        public = tool.project(self.graph, 'public')
        self.assertEqual(len(public['nodes']), 2)
        self.assertEqual(len(public['edges']), 1)
        self.assertEqual(public['revision'], 1)
        for output in (tool.encoded(public), tool.viewer(public, 'public')):
            self.assertNotIn(b'CANARY', output)
            self.assertNotIn(self.b['id'].encode(), output)
        self.assertEqual(self.graph['revision'], 17)
        self.assertEqual(len(self.graph['nodes']), 3)

    def test_private_retains_classifications(self):
        self.assertEqual(tool.project(self.graph, 'private'), self.graph)

    def test_record_gate_overrides_field(self):
        self.a['visibility'] = 'unclassified'
        result = tool.project(self.graph, 'public')
        self.assertEqual([n['id'] for n in result['nodes']], [self.c['id']])
        self.assertEqual(result['edges'], [])

    def test_missing_public_label_excludes_node_and_edges(self):
        self.c['fields']['label']['visibility'] = 'private'
        result = tool.project(self.graph, 'public')
        self.assertEqual(len(result['nodes']), 1)
        self.assertEqual(result['edges'], [])

    def test_private_relation_excludes_edge(self):
        self.graph['edges'][1]['fields']['relation']['visibility'] = 'private'
        self.assertEqual(tool.project(self.graph, 'public')['edges'], [])

    def test_rejects_bypass_metadata(self):
        for obj in (self.graph, self.a, self.a['fields']['label']):
            obj['extra'] = 'bad'
            with self.assertRaises(ValueError):
                tool.validate(self.graph)
            del obj['extra']

    def test_invalid_visibility_ids_and_endpoints(self):
        for mutate in (
            lambda g: g['nodes'][0].update(visibility='published'),
            lambda g: g['nodes'][0].update(id='person:secret-name'),
            lambda g: g['edges'][0].update(target=uid()),
            lambda g: g['nodes'].append(copy.deepcopy(g['nodes'][0])),
            lambda g: g.update(revision=True),
        ):
            graph = copy.deepcopy(self.graph)
            mutate(graph)
            with self.assertRaises(ValueError):
                tool.validate(graph)

    def test_script_escape_and_no_external_assets(self):
        self.a['fields']['label'] = field('</script><script>alert(1)</script>')
        html = tool.viewer(tool.project(self.graph, 'public'), 'public').decode()
        payload = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1)
        self.assertNotIn('<', payload)
        self.assertEqual(json.loads(payload)['nodes'][0]['fields']['label']['value'], self.a['fields']['label']['value'])
        self.assertIn("connect-src 'none'", html)
        self.assertNotRegex(html, r'<(?:script|link|iframe|img)[^>]+(?:src|href)=')

    def test_cli_success_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'master.json'
            source.write_bytes(tool.encoded(self.graph))
            args = [sys.executable, str(Path(tool.__file__)), 'export', str(source), '--audience', 'public', '--output', str(root/'export.json'), '--viewer', str(root/'viewer.html')]
            first = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(len(json.loads(first.stdout)['files']), 2)
            second = subprocess.run(args, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(tool.load(source), self.graph)

    def test_duplicate_keys_and_nonfinite_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)/'bad.json'
            for text in ('{"a":1,"a":2}', '{"a":NaN}'):
                p.write_text(text)
                with self.assertRaises(ValueError):
                    tool.load(p)

    def test_update_preserves_identity_and_reassesses_public_field(self):
        candidate = copy.deepcopy(self.graph)
        candidate['revision'] += 1
        candidate['nodes'][0]['fields']['label'] = field('Changed identity label', 'unclassified')
        candidate['nodes'][0]['fields']['update_evidence'] = field('Synthetic correction source', 'private')
        tool.validate(candidate)
        self.assertEqual(candidate['graph_id'], self.graph['graph_id'])
        self.assertEqual([n['id'] for n in candidate['nodes']], [n['id'] for n in self.graph['nodes']])
        self.assertEqual(candidate['nodes'][1:], self.graph['nodes'][1:])
        public = tool.project(candidate, 'public')
        self.assertNotIn(self.a['id'], {n['id'] for n in public['nodes']})
        self.assertNotIn(b'Synthetic correction source', tool.encoded(public))

    def test_all_unclassified_graph_exports_empty(self):
        for n in self.graph['nodes']:
            n['visibility'] = 'unclassified'
        result = tool.project(self.graph, 'public')
        self.assertEqual(result['nodes'], [])
        self.assertEqual(result['edges'], [])
        self.assertEqual(result['fields'], {})
        self.assertIn(b'No entities in this export.', tool.viewer(result, 'public'))

    def test_output_aliases_and_master_overwrite_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'master.json'
            original = tool.encoded(self.graph)
            source.write_bytes(original)
            prefix = [sys.executable, str(Path(tool.__file__)), 'export', str(source), '--audience', 'public']
            for outputs in ([str(source), str(root/'new.html')], [str(root/'same'), str(root/'same')]):
                result = subprocess.run(prefix + ['--output', outputs[0], '--viewer', outputs[1]], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(source.read_bytes(), original)
            self.assertFalse((root/'same').exists())


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.legacy = {
            'format': 'personal_property_graph',
            'title': 'Synthetic legacy graph',
            'sources': [{'id': 'source:note', 'detail': 'Legacy source'}],
            'nodes': [{'id': 'person:alex', 'type': 'Person', 'label': 'Alex', 'properties': {'job': 'Architect'}, 'source_ids': ['source:note']}],
            'edges': [],
            'private_context': {
                'nodes': [{'id': 'person:sam', 'type': 'Person', 'label': 'Sam'}],
                'edges': [{'id': 'edge:family', 'source': 'person:alex', 'target': 'person:sam', 'type': 'FAMILY_OF'}],
                'subject_attributes': {'salary': 'Synthetic private value'},
            },
        }

    def test_conservative_migration_and_fidelity(self):
        original = copy.deepcopy(self.legacy)
        graph = tool.migrate(self.legacy)
        self.assertEqual(self.legacy, original)
        self.assertEqual([n['visibility'] for n in graph['nodes']], ['unclassified', 'private'])
        self.assertEqual(graph['edges'][0]['visibility'], 'private')
        mapping = graph['fields']['legacy_id_map']['value']
        self.assertEqual(graph['edges'][0]['source'], mapping['nodes']['person:alex'])
        self.assertEqual(graph['edges'][0]['target'], mapping['nodes']['person:sam'])
        self.assertEqual(graph['nodes'][0]['fields']['legacy_record']['value'], self.legacy['nodes'][0])
        self.assertEqual(graph['fields']['legacy_private_context']['value']['subject_attributes'], self.legacy['private_context']['subject_attributes'])
        self.assertEqual(tool.project(graph, 'public')['nodes'], [])
        self.assertEqual(tool.project(graph, 'public')['fields'], {})

    def test_selective_promotion_does_not_leak_legacy_payload(self):
        graph = tool.migrate(self.legacy)
        subject = graph['nodes'][0]
        subject['visibility'] = 'public'
        for key in ('label', 'type'):
            subject['fields'][key]['visibility'] = 'public'
        public = tool.project(graph, 'public')
        self.assertEqual(len(public['nodes']), 1)
        self.assertEqual(set(public['nodes'][0]['fields']), {'label', 'type'})
        self.assertNotIn(b'Legacy source', tool.viewer(public, 'public'))
        self.assertNotIn(b'person:alex', tool.encoded(public))

    def test_invalid_legacy_inputs_rejected(self):
        for mutate in (
            lambda g: g.update(format='other'),
            lambda g: g['nodes'].append(copy.deepcopy(g['nodes'][0])),
            lambda g: g['private_context']['edges'][0].update(target='unknown'),
            lambda g: g['nodes'][0].update(label=''),
        ):
            graph = copy.deepcopy(self.legacy)
            mutate(graph)
            with self.assertRaises(ValueError):
                tool.migrate(graph)

    def test_migration_cli_roundtrip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, dest = root/'legacy.json', root/'classified.json'
            source.write_text(json.dumps(self.legacy))
            result = subprocess.run([sys.executable, str(Path(tool.__file__)), 'migrate', str(source), '--output', str(dest)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(tool.load(dest)['nodes']), 2)
            self.assertEqual(json.loads(source.read_text()), self.legacy)


if __name__ == '__main__':
    unittest.main()
