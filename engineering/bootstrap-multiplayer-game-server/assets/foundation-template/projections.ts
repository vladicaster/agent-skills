import type {
  CanonicalGameState,
  ProjectionEnvelope,
  UtcInstant,
  ViewerContext,
} from "./domain-contracts";

export interface ProjectionPolicy<TState, TView> {
  projectPublic(state: CanonicalGameState<TState>): TView;
  projectMember(state: CanonicalGameState<TState>, viewer: ViewerContext): TView;
  projectPlayerPrivate(
    state: CanonicalGameState<TState>,
    viewer: ViewerContext,
  ): TView;
  projectHost(state: CanonicalGameState<TState>, viewer: ViewerContext): TView;
  projectAdministrator(
    state: CanonicalGameState<TState>,
    viewer: ViewerContext,
  ): TView;
}

export function projectForViewer<TState, TView>(
  state: CanonicalGameState<TState>,
  viewer: ViewerContext,
  serverTime: UtcInstant,
  projectionVersion: number,
  policy: ProjectionPolicy<TState, TView>,
): ProjectionEnvelope<TView> {
  let view: TView;

  if (viewer.isAdministrator) {
    view = policy.projectAdministrator(state, viewer);
  } else if (viewer.membership?.role === "host") {
    view = policy.projectHost(state, viewer);
  } else if (viewer.membership?.role === "player") {
    view = policy.projectPlayerPrivate(state, viewer);
  } else if (viewer.membership?.status === "active") {
    view = policy.projectMember(state, viewer);
  } else {
    view = policy.projectPublic(state);
  }

  return {
    sessionId: state.sessionId,
    projectionVersion,
    revision: state.revision,
    serverTime,
    view,
  };
}
