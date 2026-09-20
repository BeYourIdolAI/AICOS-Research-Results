# AICOS Diagnosticity Method Pack

## WHAT THIS IS

A candidate Measurement Assurance / Night Lab research-method package for
checking whether an experiment fixture is diagnostic of its attack variable.

## WHAT THIS IS NOT

It is not an EAW patch, v0.4.9 proposal, normative primitive, closure action,
independent validation, replacement for raw experiment outputs or proof that
the method is correct.

## WHY IT EXISTS

AT4-01, AT1-01 and AT3-01 repeatedly showed that execution or local rule
discrimination can fail to establish that the intended attack variable was
actually isolated.

## HOW TO USE IT BEFORE A NIGHT LAB RUN

Read the cross-experiment review, then run D1–D11 before execution. Record
fixture facts, frozen text, dependencies, control viability, blocker behavior,
types, outcome layers and falsifiability. Stop when a gate fails.

## HOW TO INTERPRET PASS/FAIL

PASS/FAIL is available only after the diagnosticity gates pass.

Use the more specific vocabulary when appropriate:

VALID AND DIAGNOSTIC
VALID BUT NON-DIAGNOSTIC
INVALID TRACE
AMBIGUOUS
BLOCKED
NON-DIAGNOSTIC BY CONSTRUCTION
ORTHOGONAL BLOCKER
TAUTOLOGICAL BLOCKER
UNRESOLVED SEMANTIC RELATION

## RELATION TO EAW

D1–D11 are a non-normative test-method contract. They are not EAW contract
text and do not change EAW v0.4.8.

## RELATION TO TRUST DEPENDENCY PRESERVATION

The package does not establish whether Trust Dependency Preservation exists,
is required or is implemented.

## CURRENT STATUS

CANDIDATE RESEARCH METHOD
NOT FROZEN
NOT INDEPENDENTLY VALIDATED

## START HERE

1. AICOS_DIAGNOSTICITY_CROSS_EXPERIMENT_REVIEW_v0.1.md
2. AICOS_DIAGNOSTICITY_PREFLIGHT_v0.1.md
3. AICOS_DIAGNOSTICITY_RESEARCH_NOTES_v0.1.md

## HISTORICAL PRESERVATION

AT4-01, AT1-01, AT3-01, EAW v0.4.8, P4, Trust Dependency and bootstrap
artifacts are not modified by this package.

Proposed repository path:

measurement-assurance/diagnosticity/

Proposed commit message:

research(measurement-assurance): add diagnosticity preflight candidate v0.1
