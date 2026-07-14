# Goal Brainstorm Document Contract

## Document Owners

- Applicable `AGENTS.md` files own durable project instructions and engineering constraints for their path scope.
- `doc/design.md` and `doc/design/**.md` own stable architecture and project contracts.
- `doc/spec/**` owns task-specific implementation requirements that do not naturally belong to existing instruction or design owners.
- `doc/goal/**` owns one concise executable objective and exact references to its approved source contracts.

A goal is not a second design or specification owner. A specification must not copy durable instructions or architecture already owned elsewhere.

## Document Selection

A multi-repository change has one coordinating repository that owns its dedicated implementation specification and goal. Coordination ownership must follow the current project contracts or an explicit user decision.

Use **Direct Owner Update** when the change is a small amendment to existing instructions, design, or specification, or when even a substantial change belongs completely and naturally to one or two existing owner documents. Update those owners and make the goal reference the exact changed sections. Do not create a specification merely to restate them.

Use **Dedicated Implementation Specification** when the task has a substantial standalone brief, spans several owners, needs one task-level migration or rollout contract, carries shared acceptance criteria across components, or would pollute stable owner documents with implementation-specific constraints. Existing owner documents may still change, but the new specification owns only the integrating task-specific requirements.

If user intent conflicts with a current owner, change that owner after approval rather than hiding the conflict in a new specification.

## File Names

Create new files with their creation date and a stable semantic name:

```text
doc/spec/YYYY-MM-DD-<semantic-name>.md
doc/goal/YYYY-MM-DD-<semantic-name>.md
```

Do not rename an existing dated specification when updating it later. A new goal uses its own creation date and may reference an older specification. Update an existing goal file only while continuing the same inactive objective. Create a current-date goal for a new objective or a follow-up to a completed objective. Reuse a same-day path only for the same task; choose a more precise semantic name for a different task instead of adding a numeric suffix.

## Implementation Specification

Use a structure shaped by the task rather than a mandatory heading template. Include every applicable semantic element:

- required outcome and problem;
- verified current state;
- scope and non-goals;
- approved decisions and their rationale;
- target behavior;
- public interfaces, models, and data owners;
- state transitions for stateful behavior;
- failure handling and recovery;
- migration and compatibility;
- changes by repository or owner component;
- verification obligations and observable acceptance criteria required by `Verification Design`.

The approved specification describes the final steady state. It must not retain rejected alternatives, open questions, `TODO` markers, placeholders, compatibility bridges that are not part of the target, or a step-by-step implementation plan.

## Verification Design

Design verification before approving each changed observable behavior. Apply the affected project's existing test and verification contracts by reference instead of restating their framework, placement, fixtures, or command rules. For every changed observable behavior, the approved owner documents must identify:

- the observable contract or outcome;
- the verification owner and the appropriate unit, integration, workflow, migration, semantic, or operational level;
- the success path, primary contract-defining failure path, and critical new edge cases;
- required data, environment, or external dependencies and an exact stable command when one exists.

For changed executable behavior, the approved owner documents must require adding or updating automated behavior tests whenever those tests are direct evidence of correctness. Existing tests satisfy this obligation only when the verification design identifies how they already exercise every changed contract branch. Name a concrete test file only when that path is itself a stable owner; otherwise identify the owning test family or verification boundary.

Automated tests must verify executable behavior and public contracts rather than private call sequences, incidental class or file layout, or mocked interactions used as a substitute for required boundary behavior.

Instruction, design, and specification artifacts are verified through semantic reread or semantic audit. Never design pytest assertions over their prose, headings, examples, file presence, or placement.

When automated testing is not appropriate, specify the exact semantic or operational verification and why it is sufficient. If a requirement cannot be observed unambiguously, refine its interface or acceptance criteria before approval. The brainstorm writes no test code and must not turn verification design into a step-by-step implementation plan.

## Goal File

Keep the goal materially below the persistent objective limit and use this shape:

```markdown
# <Result name>

## Outcome

<Concrete final state.>

## Source Contracts

- `<resolvable path>`: `<exact section or document role>`

## Constraints

<Only task-specific boundaries not already expressed by the source references.>

## Verification

<Verifiable completion definition or exact references to its owners.>
```

The `Verification` section must reference the approved verification obligations and every applicable project test-contract owner without copying their rules.

The goal states the outcome, essential constraints, and verification while giving Codex exact file context and freedom to build and revise its working plan. It must not copy source contracts, predict a brittle implementation-file list, or split one multi-repository objective into several goals.

Use root-relative paths for contracts in the coordinating repository. Use absolute paths for contracts in other repositories so every cross-repository reference resolves without guessing a repository root.

The persistent objective should name the goal file, treat it as the completion contract, and require the full applicable verification and final semantic review. Keep detailed context in project files instead of expanding the objective.

## Semantic Review

Before creating the goal, reread all changed and directly affected documents as one contract set. Confirm that:

- each requirement has one owner;
- references identify exact source documents or sections without duplicating their content;
- public interfaces and ownership boundaries are explicit;
- state transitions, failure behavior, and recovery are complete when applicable;
- verification design satisfies `Verification Design` for every changed observable behavior;
- no open decision, contradiction, unnecessary wrapper, duplicated carrier, or transition-only target remains.
