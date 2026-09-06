PRAGMA foreign_keys = ON;

CREATE TABLE game_sessions (
    session_id TEXT PRIMARY KEY,
    game_definition_id TEXT NOT NULL,
    state_schema_version INTEGER NOT NULL CHECK (state_schema_version > 0),
    revision INTEGER NOT NULL DEFAULT 0 CHECK (revision >= 0),
    status TEXT NOT NULL,
    deadline_utc TEXT NULL,
    content_version_id TEXT NULL,
    created_utc TEXT NOT NULL,
    updated_utc TEXT NOT NULL
);

CREATE TABLE session_memberships (
    membership_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL REFERENCES game_sessions(session_id),
    subject_id TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('host', 'player', 'observer')),
    status TEXT NOT NULL CHECK (status IN ('invited', 'active', 'left', 'removed')),
    joined_utc TEXT NULL,
    last_seen_utc TEXT NULL,
    UNIQUE (session_id, subject_id)
);

CREATE UNIQUE INDEX ux_session_active_host
ON session_memberships(session_id)
WHERE role = 'host' AND status = 'active';

CREATE TABLE game_state_snapshots (
    session_id TEXT NOT NULL REFERENCES game_sessions(session_id),
    revision INTEGER NOT NULL CHECK (revision >= 0),
    schema_version INTEGER NOT NULL CHECK (schema_version > 0),
    state_json TEXT NOT NULL,
    state_hash TEXT NOT NULL,
    created_utc TEXT NOT NULL,
    PRIMARY KEY (session_id, revision)
);

CREATE TABLE accepted_game_events (
    event_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL REFERENCES game_sessions(session_id),
    revision INTEGER NOT NULL CHECK (revision > 0),
    event_sequence INTEGER NOT NULL DEFAULT 0 CHECK (event_sequence >= 0),
    event_type TEXT NOT NULL,
    event_version INTEGER NOT NULL CHECK (event_version > 0),
    actor_subject_id TEXT NULL,
    command_id TEXT NULL,
    payload_json TEXT NOT NULL,
    occurred_utc TEXT NOT NULL,
    UNIQUE (session_id, revision, event_sequence)
);

CREATE TABLE command_receipts (
    session_id TEXT NOT NULL REFERENCES game_sessions(session_id),
    command_id TEXT NOT NULL,
    actor_subject_id TEXT NOT NULL,
    command_type TEXT NOT NULL,
    expected_revision INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('processing', 'accepted', 'rejected')),
    resulting_revision INTEGER NULL,
    result_code TEXT NULL,
    safe_result_json TEXT NULL,
    created_utc TEXT NOT NULL,
    completed_utc TEXT NULL,
    PRIMARY KEY (session_id, command_id)
);

CREATE TABLE generation_jobs (
    generation_job_id TEXT PRIMARY KEY,
    session_id TEXT NULL REFERENCES game_sessions(session_id),
    status TEXT NOT NULL,
    current_stage TEXT NOT NULL,
    schema_version INTEGER NOT NULL CHECK (schema_version > 0),
    prompt_version TEXT NOT NULL,
    model_id TEXT NOT NULL,
    attempt_count INTEGER NOT NULL DEFAULT 0 CHECK (attempt_count >= 0),
    repair_count INTEGER NOT NULL DEFAULT 0 CHECK (repair_count >= 0),
    input_tokens INTEGER NOT NULL DEFAULT 0 CHECK (input_tokens >= 0),
    output_tokens INTEGER NOT NULL DEFAULT 0 CHECK (output_tokens >= 0),
    estimated_cost_micros INTEGER NOT NULL DEFAULT 0 CHECK (estimated_cost_micros >= 0),
    max_cost_micros INTEGER NOT NULL CHECK (max_cost_micros >= 0),
    lease_owner TEXT NULL,
    lease_expires_utc TEXT NULL,
    failure_category TEXT NULL,
    created_utc TEXT NOT NULL,
    updated_utc TEXT NOT NULL
);

CREATE TABLE generation_checkpoints (
    generation_job_id TEXT NOT NULL REFERENCES generation_jobs(generation_job_id),
    stage TEXT NOT NULL,
    checkpoint_version INTEGER NOT NULL CHECK (checkpoint_version > 0),
    input_hash TEXT NOT NULL,
    output_hash TEXT NOT NULL,
    artifact_reference TEXT NULL,
    validated INTEGER NOT NULL CHECK (validated IN (0, 1)),
    validation_json TEXT NOT NULL,
    created_utc TEXT NOT NULL,
    PRIMARY KEY (generation_job_id, stage)
);

CREATE TABLE game_audit_records (
    audit_id TEXT PRIMARY KEY,
    session_id TEXT NULL REFERENCES game_sessions(session_id),
    actor_subject_id TEXT NULL,
    action_type TEXT NOT NULL,
    attempted_revision INTEGER NULL,
    outcome TEXT NOT NULL,
    correlation_id TEXT NULL,
    safe_details_json TEXT NOT NULL,
    occurred_utc TEXT NOT NULL
);

CREATE INDEX ix_memberships_subject ON session_memberships(subject_id, status);
CREATE INDEX ix_generation_jobs_status ON generation_jobs(status, updated_utc);
CREATE INDEX ix_audit_session_time ON game_audit_records(session_id, occurred_utc);
