# AICOS Diagnosticity Preflight v0.1

TITLE:
AICOS Diagnosticity Preflight v0.1

STATUS:
CANDIDATE RESEARCH METHOD

NORMATIVE STATUS:
NON-NORMATIVE

FREEZE STATUS:
NOT FROZEN

VALIDATION STATUS:
NOT INDEPENDENTLY VALIDATED

SCOPE:
Measurement Assurance / Night Lab experiment design

NOT PART OF:
EAW normative contract

## Purpose

This preflight separates mechanical execution and local rule application from
whether a fixture is actually diagnostic of the attack variable.

It is an additive research method. It does not replace raw experiment
outputs, historical results or reviews.

## Core distinctions

MECHANICAL EXECUTION
≠
DIAGNOSTIC EXPERIMENT

RULE DISCRIMINATION
≠
ATTACK DISCRIMINATION

TRACE EXECUTED
≠
TRACE VALID

TRACE VALID
≠
TRACE DIAGNOSTIC

TRACE DIAGNOSTIC
≠
ATTACK CLASS ESTABLISHED

ATTACK CLASS ESTABLISHED
≠
DESIGN DEFECT

DESIGN DEFECT
≠
NEW PRIMITIVE REQUIRED

All are candidate research principles, non-normative, not validated and not
EAW contract text.

## D1 — SAME TARGET

Control and attack arms must attempt the same proposition and epistemic status.
If target, claim or attempted decision differs:

INVALID EXPERIMENT DESIGN.

## D2 — SINGLE AXIS

Only the attack variable may differ. Hold constant where applicable claim,
interval, scope, contract, threat model, prerequisites, evidence, attempted
decision, identities and semantic interpretation.

If more than one causal axis changes:

INVALID EXPERIMENT DESIGN.

## D3 — EXPLICIT DEPENDENCY

Every load-bearing dependency must be established by frozen text or declared as
a fixture fact.

Record SOURCE as TEXT or FIXTURE and the inference class as DIRECT,
DEFINITIONAL, LOGICALLY NECESSARY, DERIVED or NEW RULE.

DERIVED / NEW RULE cannot carry PASS/FAIL unless the semantic gap itself is the
test object.

## D4 — CONTROL VIABILITY

H_FULL/control must be independently conformant before attack evaluation.

If control fails for an axis-independent reason:

INVALID TRACE
or
NON-DIAGNOSTIC FIXTURE.

## D5 — ATTACK-SENSITIVE BLOCKER

For blocker B:

B(H_CONTROL) = FALSE
B(H_ATTACK) = TRUE

TRUE / TRUE is an ORTHOGONAL BLOCKER.
FALSE / FALSE makes the blocker irrelevant.
UNRESOLVED / anything prevents determinate PASS/FAIL.

## D6 — NON-TAUTOLOGICAL DISCRIMINATION

The varied attack variable must not be identical to the blocker's antecedent,
the rule's acceptance predicate or the exact condition named by the rule.

If the arms are defined by the rule antecedent:

NON-DIAGNOSTIC BY CONSTRUCTION.

## D7 — NO CONCLUSION STIPULATION

Fixture facts may stipulate world state, identities, timing, boundaries and
controlled inputs.

They may not stipulate attack success, attack failure, blocker outcome or the
proposition whose discovery is the result.

Otherwise:

INVALID / TAUTOLOGICAL DESIGN.

## D8 — TYPE PRESERVATION

Preserve:

CLAIM
≠
EVIDENCE
≠
ASSESSMENT
≠
METADATA

Any substitution requires exact contract support.

## D9 — SEMANTIC COMPLETENESS

Before PASS/FAIL, identify every load-bearing term, threshold, prerequisite and
semantic relation.

Unresolved relation in frozen text:

AMBIGUOUS.

Required but neither established nor legitimately stipulated:

INVALID TRACE.

## D10 — OUTCOME-LAYER SEPARATION

Keep distinct:

- NORMATIVE CONFORMANCE
- VERIFIABILITY / DETECTABILITY
- RUNTIME PREVENTION / ENFORCEMENT

Do not infer one from another.

## D11 — FALSIFIABILITY CHECK

Before execution, identify a fixture-consistent world producing a different
result.

If no such world exists:

NON-DIAGNOSTIC BY CONSTRUCTION.

## Result vocabulary

Use:

- VALID AND DIAGNOSTIC
- VALID BUT NON-DIAGNOSTIC
- INVALID TRACE
- AMBIGUOUS
- BLOCKED
- LOCAL NORMATIVE APPLICATION ONLY
- NON-DIAGNOSTIC BY CONSTRUCTION
- ORTHOGONAL BLOCKER
- TAUTOLOGICAL BLOCKER
- UNRESOLVED SEMANTIC RELATION

PASS/FAIL is available only after the diagnosticity gates pass.

## Pre-execution checklist

Confirm same target, single axis, explicit dependencies, viable control,
attack-sensitive blocker, non-tautological discrimination, no conclusion
stipulation, type preservation, semantic completeness, outcome-layer
separation and falsifiability.

## Post-execution checklist

Record raw trace identity, fixture facts, frozen text, inference classes,
control and attack outcomes, blocker table, diagnosticity result, missing
evidence, limitations and reviewer provenance.

## STOP conditions

STOP if a new judgment is required, a dependency is unresolved, control is
non-viable, the blocker is orthogonal, discrimination is tautological, the
conclusion is stipulated, types are substituted, or falsifiability fails.

Do not promote a local result into an attack-class or general claim without
additional evidence.

## Provenance

This candidate method is derived from the AT4-01, AT1-01 and AT3-01 experiment
histories, design-adjacent adversarial review, mechanical verification,
ChatGPT/Sol analysis and human-directed synthesis.

It is not independently validated.
