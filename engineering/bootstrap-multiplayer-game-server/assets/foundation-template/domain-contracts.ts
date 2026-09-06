export type EntityId = string;
export type UtcInstant = string;

export type SessionStatus =
  | "creating"
  | "ready"
  | "active"
  | "paused"
  | "completed"
  | "failed"
  | "cancelled";

export interface SessionMember {
  membershipId: EntityId;
  sessionId: EntityId;
  subjectId: EntityId;
  role: "host" | "player" | "observer";
  status: "invited" | "active" | "left" | "removed";
  joinedAt: UtcInstant | null;
  lastSeenAt: UtcInstant | null;
}

export interface CanonicalGameState<TPayload> {
  sessionId: EntityId;
  gameDefinitionId: EntityId;
  schemaVersion: number;
  revision: number;
  status: SessionStatus;
  createdAt: UtcInstant;
  updatedAt: UtcInstant;
  deadlineAt: UtcInstant | null;
  contentVersionId: EntityId | null;
  payload: TPayload;
}

export interface AcceptedGameEvent<TPayload> {
  eventId: EntityId;
  eventType: string;
  eventVersion: number;
  sessionId: EntityId;
  revision: number;
  actorSubjectId: EntityId | null;
  commandId: EntityId | null;
  occurredAt: UtcInstant;
  payload: TPayload;
}

export interface ViewerContext {
  subjectId: EntityId | null;
  membership: SessionMember | null;
  isAdministrator: boolean;
}

export interface ProjectionEnvelope<TView> {
  sessionId: EntityId;
  projectionVersion: number;
  revision: number;
  serverTime: UtcInstant;
  view: TView;
}

export interface ServerClock {
  now(): UtcInstant;
}
