# Harness Patterns

## Minimal repository

Use a root `AGENTS.md`, verified build and test commands, and the existing contribution template when one team and one stack share uniform rules.

## Documented application

Use concise root instructions, architecture and engineering references, workflow templates, and optional host adapters when standards require detailed explanation.

## Monorepo

Use shared root instructions plus nested instructions only for materially different packages. Avoid repeating root rules in every package.

## Greenfield package

Use provisional instructions, an architecture and stack decision, engineering strategies, workflow templates, and a manifest with assumptions. Reconcile after repository creation.
