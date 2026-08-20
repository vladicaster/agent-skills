---
name: develop-go-to-market-strategy
description: Develop, audit, refine, diagnose, launch-plan, and reconcile evidence-based go-to-market strategies for products and services. Use when a user wants to turn a product idea, PRD, website, pitch deck, customer evidence, existing GTM plan, or performance results into market segmentation, ICP, positioning, messaging, packaging, pricing hypotheses, sales motions, channels, launch plans, experiments, readiness gaps, and measurable 30/60/90-day priorities.
---

# Develop Go-to-Market Strategy

Create a decision-ready strategy that connects product, market, offer, distribution, sales, customer success, and measurement. Separate verified evidence, company-provided facts, inference, and assumptions.

## Select the mode

- **Discover:** Form an initial commercialization hypothesis from an idea or PRD.
- **Develop:** Produce a complete GTM strategy.
- **Audit:** Evaluate an existing strategy without changing external systems.
- **Refine:** Update a strategy using new constraints or evidence.
- **Launch:** Convert an approved strategy into a phased launch plan.
- **Diagnose:** Analyze weak acquisition, activation, conversion, retention, or expansion.
- **Reconcile:** Update strategy using actual market results.

Default to Audit or Diagnose when the user asks why an existing effort is underperforming.

## Phase 1: Establish the decision context

1. Confirm the product, maturity, business model, geography, revenue objective, timeline, team, budget, delivery capacity, and definition of success.
2. Confirm the output destination. GitHub is not required; use a document or portable artifact unless the user approves a repository-backed destination. Before repository writes, verify the authenticated identity, repository, visibility compatibility, and required permissions. Report missing access as **Blocked** for that write without blocking the strategy itself.
3. Gather available evidence: PRD, website, pitch deck, customer interviews, usage data, sales results, competitor list, current messaging, and existing GTM plan.
4. Identify missing decisions. Ask only questions that materially affect segmentation, offer, motion, or economics.
5. When current market facts matter, research authoritative and recent sources. Cite factual claims and label inference.

## Phase 2: Assess readiness and market

1. Read `references/market-readiness.md` and determine whether problem, product, buyer, proof, delivery, offer, and measurement are launch-ready.
2. Identify direct competitors, indirect alternatives, substitutes, category language, buyer behavior, and market constraints.
3. Classify each gap as **launch blocker**, **near-term requirement**, **experiment**, **later enhancement**, or **not justified**.

## Phase 3: Choose the market and position

1. Read `references/segmentation-and-icp.md`.
2. Score candidate segments using problem intensity, urgency, willingness to pay, reachability, product fit, proof, expansion potential, and cost to serve. Run `scripts/score_segments.py` when structured segment data is available.
3. Recommend one beachhead segment, one secondary segment when justified, and explicitly deferred segments.
4. Define the ICP, end user, economic buyer, technical evaluator, influencers, blockers, trigger events, alternatives, objections, and buying criteria.
5. Read `references/positioning-and-messaging.md` and develop a supportable category, differentiated promise, reasons to believe, proof, narrative, and objection handling.

## Phase 4: Design the offer and motion

1. Read `references/offers-and-pricing.md` and propose packaging, pricing hypotheses, entry offer, trial/demo/pilot, onboarding, time to value, support, retention, and expansion.
2. Read `references/channels-and-motions.md`.
3. Recommend the appropriate founder-led, product-led, sales-led, partner-led, community-led, content-led, marketplace-led, or hybrid motion.
4. Rank channels. For each selected channel, state the segment, funnel stage, message, offer, assets, effort, expected learning, metric, and stop/scale threshold.
5. Do not recommend a broad channel list without prioritization or operational feasibility.

## Phase 5: Present the strategy for approval

Present:

- executive recommendation
- evidence and assumptions
- market readiness and launch blockers
- primary and secondary segments
- ICP and buying group
- positioning and messaging
- packaging and pricing hypotheses
- sales motion and ranked channels
- customer journey and success model
- product, business, and measurement gaps
- risks and dependencies
- proposed experiments and 30/60/90-day plan

Ask the user to **approve**, **revise**, or **cancel** before treating the strategy as the launch baseline.

## Phase 6: Build the approved launch and measurement plan

1. Read `references/launch-planning.md` and `references/measurement-and-experiments.md`.
2. Define phases, owners, dependencies, assets, budget assumptions, decision gates, and operational readiness.
3. Define acquisition, activation, conversion, retention, expansion, and economic measures appropriate to the business model.
4. Make each experiment falsifiable with a hypothesis, audience, intervention, metric, threshold, duration, and next decision.
5. Report evidence gaps, unresolved risks, and decisions that remain provisional.

## Boundaries

- Do not fabricate market size, competitor capabilities, customer evidence, pricing, conversion rates, or unit economics.
- Do not confuse market size with reachable near-term opportunity.
- Do not recommend paid acquisition before the offer, conversion path, measurement, and delivery capacity are credible.
- Do not optimize for activity volume instead of learning and commercial outcomes.
- Do not contact prospects, send messages, publish content, purchase advertising, alter pricing, edit production systems, update a CRM, create external accounts, or commit to partners without separate authorization.
- Treat pricing, revenue, CAC, conversion, and timing figures without evidence as hypotheses.
- Keep strategy portable across industries while adapting rigor to regulation, buying complexity, contract value, and sales cycle.
