# AICOS Diagnosticity Cross-Experiment Review v0.1

STATUS:
RESEARCH REVIEW LAYER

NORMATIVE STATUS:
NON-NORMATIVE

VALIDATION STATUS:
NOT INDEPENDENTLY VALIDATED

## 1. SCOPE

This review preserves methodological lessons from AT4-01, AT1-01 and AT3-01.
It does not rewrite their historical records or replace raw outputs.

## 2. SOURCE OBJECTS

- AT4-01
- AT1-01
- AT3-01
- associated design-adjacent adversarial review
- associated mechanical verification
- ChatGPT/Sol analysis
- human-directed synthesis

Exact raw source files were not supplied as part of this method package.
This review does not reconstruct them.

## 3. REVIEW ROLE

This is a design-adjacent synthesis, not independent validation.

Model agreement is provenance, not proof.

## 4. AT4-01 SUMMARY

RUN-01:
INVALID TRACE / PRESERVED

Corrected run:
AMBIGUOUS WITHIN TEST SCOPE

Claim boundary:
C2 supported within test scope, conditional on fixture stipulation S1.

S1 stipulates that the transition occurs at an actual observer,
observation-epoch and storage-instance boundary.

S1 is a fixture stipulation, not an EAW transition-trigger rule.

Unresolved semantic relation:

Whether P, carried only as a named trust assumption under §15.1, is
sufficient support for §16.1 rad 592's required gap/restart condition
("ska vara styrkta").

AT-4:
CANDIDATE / NOT ESTABLISHED

Verifiability:
UNEXAMINED

Runtime prevention:
NOT ESTABLISHED

Design action:
NONE

Methodological findings:
- fixture facts must be distinguished from contract-established rules;
- blocker ordering alone is insufficient;
- control/attack discrimination must be demonstrated;
- normative conformance, detectability and runtime prevention are distinct.

## 5. AT1-01 SUMMARY

Sonnet primary result:
FAIL — EXPLICIT RULE DISCRIMINATES H_FULL FROM H_DROP

Final adversarial review:
INVALID TRACE / PRIMARY RESULT REJECTED

Object verification:
COMPLETE

F-AT1-01:
C-G3 failed. §15.1 rad 522 conditionally refers to P but does not establish
that coverage boundary B depends on P.

F-AT1-02:
The direct NSAV hook was misidentified. §6 rad 210 explicitly extends NSAV
to §§4–5, §13, §16.1 and applicable §9.0 prerequisites, but does not
explicitly name §14.

F-AT1-03:
Control derivation was not established. §15.1 rad 530 establishes that
trust-carried P is not thereby established; it does not establish that B is
not positively established.

F-AT1-04:
The discrimination table varied both information state and attempted
attribution, so it did not isolate the provenance/drop axis.

AT-1:
CANDIDATE / NOT ESTABLISHED

Methodological findings:
- conditional text must not be treated as establishing its antecedent;
- section-level hooks must be mechanically verified;
- control derivation must be established;
- one must not vary multiple causal axes;
- mechanical verification may weaken a claim.

## 6. AT3-01 SUMMARY

Sonnet primary result:
FAIL — EXPLICIT RULE DISCRIMINATES H_FULL FROM H_CIRC

Adversarial review:
Trace VALID

Local normative application:
VALID

AT-3 falsification:
NON-INFORMATIVE BY CONSTRUCTION

§12 rad 457 directly blocks constructed H_CIRC where no genuinely new valid
interval-relevant evidence enters.

H_FULL had new valid interval-relevant evidence. H_CIRC did not. Because this
is the controlling predicate of §12 rad 457, the observed discrimination was
guaranteed by construction.

This is TAUTOLOGICAL DISCRIMINATION, not informative falsification.

AT-3:
CANDIDATE / NOT ESTABLISHED

## 7. CROSS-EXPERIMENT OBSERVATIONS

Observed failure modes:

1. unresolved semantic relation;
2. orthogonal blocker;
3. tautological blocker;
4. unstated dependency or prerequisite;
5. control non-viability;
6. type substitution;
7. conclusion stipulation;
8. outcome-layer collapse.

These are observations from the current test history, not universal laws.

## 8. FAILURE-MODE TAXONOMY

The taxonomy is a research organizing layer. It is not asserted exhaustive,
complete or validated.

## 9. CANDIDATE DIAGNOSTICITY PRINCIPLES

- MECHANICAL EXECUTION ≠ DIAGNOSTIC EXPERIMENT
- RULE DISCRIMINATION ≠ ATTACK DISCRIMINATION

No EAW normative change follows.

## 10. WHAT IS ESTABLISHED

SUPPORTED WITHIN CURRENT TEST HISTORY:

Across AT4-01, AT1-01 and AT3-01, fixture diagnosticity repeatedly limited
the evidential value of the experiment result.

This supports developing a candidate diagnosticity preflight.

## 11. WHAT IS NOT ESTABLISHED

- D1–D11 are complete;
- D1–D11 are sufficient;
- D1–D11 guarantee valid falsification;
- the failure modes are exhaustive;
- the method generalizes outside this experiment family;
- EAW has or lacks Trust Dependency Preservation;
- AT-1, AT-3 or AT-4 are design defects;
- a new primitive is required;
- P4 is reopened;
- EAW F-2 is closed.

## 12. LIMITATIONS

Exact raw experiment files were not supplied with this method package. The
method layer cannot replace them.

This package is not independent validation and does not prove correctness.

## 13. REVIEW PROVENANCE

The package is derived from Sonnet experiment runs, design-adjacent
adversarial review, mechanical verification, ChatGPT/Sol analysis and
human-directed synthesis.

No claim of independent validation is made.

## 14. NEXT ELIGIBLE ACTION

Human review and/or adversarial review of the diagnosticity preflight itself.

No automatic redesign, EAW patch, P4 reopening or new primitive follows.
