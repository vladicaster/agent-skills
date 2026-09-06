import type { EntityId, ProjectionEnvelope } from "./domain-contracts";

export interface GameCommand<TPayload> {
  commandId: EntityId;
  commandType: string;
  commandVersion: number;
  sessionId: EntityId;
  expectedRevision: number;
  correlationId: string | null;
  payload: TPayload;
}

export type CommandErrorCode =
  | "unauthenticated"
  | "forbidden"
  | "not_member"
  | "invalid_command"
  | "stale_revision"
  | "duplicate_in_progress"
  | "phase_closed"
  | "budget_exhausted"
  | "session_unavailable";

export type CommandResult<TView> =
  | {
      status: "accepted";
      commandId: EntityId;
      projection: ProjectionEnvelope<TView>;
    }
  | {
      status: "rejected";
      commandId: EntityId;
      code: CommandErrorCode;
      currentRevision: number | null;
      safeMessage: string;
      projection?: ProjectionEnvelope<TView>;
    };

export interface AuthenticatedCommand<TPayload> {
  actorSubjectId: EntityId;
  command: GameCommand<TPayload>;
}
