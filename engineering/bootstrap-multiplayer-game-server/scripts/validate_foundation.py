#!/usr/bin/env python3
"""Validate the generic multiplayer foundation assets without external services."""

from __future__ import annotations

import json
from pathlib import Path
import sqlite3
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "foundation-template"


def validate_schema(errors: list[str]) -> None:
    schema_path = TEMPLATE / "persistence-schema.sql"
    try:
        schema = schema_path.read_text(encoding="utf-8")
        connection = sqlite3.connect(":memory:")
        connection.executescript(schema)
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            )
        }
        required = {
            "game_sessions",
            "session_memberships",
            "game_state_snapshots",
            "accepted_game_events",
            "command_receipts",
            "generation_jobs",
            "generation_checkpoints",
            "game_audit_records",
        }
        if missing := sorted(required - tables):
            errors.append(f"schema missing tables: {', '.join(missing)}")
            return

        connection.execute(
            """INSERT INTO game_sessions
               (session_id, game_definition_id, state_schema_version, revision,
                status, created_utc, updated_utc)
               VALUES ('session-example', 'game-example', 1, 7, 'active',
                       '2026-01-01T00:00:00.000Z', '2026-01-01T00:07:00.000Z')"""
        )
        connection.execute(
            """INSERT INTO session_memberships
               (membership_id, session_id, subject_id, role, status, joined_utc)
               VALUES ('member-host-a', 'session-example', 'subject-a', 'host',
                       'active', '2026-01-01T00:00:00.000Z')"""
        )
        try:
            connection.execute(
                """INSERT INTO session_memberships
                   (membership_id, session_id, subject_id, role, status, joined_utc)
                   VALUES ('member-host-b', 'session-example', 'subject-b', 'host',
                           'active', '2026-01-01T00:00:00.000Z')"""
            )
            errors.append("schema permits two active hosts for one session")
        except sqlite3.IntegrityError:
            pass

        event_values = (
            "session-example",
            8,
            "example.event",
            1,
            "{}",
            "2026-01-01T00:08:00.000Z",
        )
        connection.execute(
            """INSERT INTO accepted_game_events
               (event_id, session_id, revision, event_sequence, event_type,
                event_version, payload_json, occurred_utc)
               VALUES ('event-1', ?, ?, 0, ?, ?, ?, ?)""",
            event_values,
        )
        connection.execute(
            """INSERT INTO accepted_game_events
               (event_id, session_id, revision, event_sequence, event_type,
                event_version, payload_json, occurred_utc)
               VALUES ('event-2', ?, ?, 1, ?, ?, ?, ?)""",
            event_values,
        )

        accepted = connection.execute(
            """UPDATE game_sessions
               SET revision = revision + 1
               WHERE session_id = 'session-example' AND revision = 7"""
        ).rowcount
        stale = connection.execute(
            """UPDATE game_sessions
               SET revision = revision + 1
               WHERE session_id = 'session-example' AND revision = 7"""
        ).rowcount
        if accepted != 1 or stale != 0:
            errors.append("revision compare-and-swap behavior is not enforceable")
    except (OSError, sqlite3.Error) as exc:
        errors.append(f"SQL validation failed: {exc}")


def validate_fixture(errors: list[str]) -> None:
    fixture_path = TEMPLATE / "contract-fixture.json"
    try:
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"contract fixture failed to parse: {exc}")
        return

    state = fixture.get("initialState", {})
    command = fixture.get("acceptedCommand", {})
    accepted = fixture.get("expectedAcceptedResult", {})
    repeated = fixture.get("expectedRepeatedResult", {})
    stale = fixture.get("expectedStaleResult", {})
    projection = fixture.get("projectionAssertions", {})

    if command.get("sessionId") != state.get("sessionId"):
        errors.append("accepted command targets a different session")
    if command.get("expectedRevision") != state.get("revision"):
        errors.append("accepted command does not use the initial revision")
    if accepted.get("resultingRevision") != state.get("revision", -1) + 1:
        errors.append("accepted result does not increment the revision once")
    if repeated.get("resultingRevision") != accepted.get("resultingRevision"):
        errors.append("idempotent repeat changes the resulting revision")
    if repeated.get("duplicateEffects") != 0:
        errors.append("idempotent repeat permits duplicate effects")
    if stale.get("code") != "stale_revision":
        errors.append("stale command fixture lacks the stable error code")
    if stale.get("currentRevision") != accepted.get("resultingRevision"):
        errors.append("stale result does not report the current revision")
    if not projection.get("mustContain") or not projection.get("mustNotContain"):
        errors.append("projection fixture must include positive and negative assertions")


def main() -> int:
    errors: list[str] = []
    validate_schema(errors)
    validate_fixture(errors)
    if errors:
        print(f"FAILED: {len(errors)} foundation validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASSED: foundation SQL and portability fixture validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
