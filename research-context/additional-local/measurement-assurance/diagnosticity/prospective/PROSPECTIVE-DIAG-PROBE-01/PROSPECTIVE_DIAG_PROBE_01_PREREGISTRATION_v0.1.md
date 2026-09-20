# PROSPECTIVE-DIAG-PROBE-01 — Preregistration

VERSION: `v0.1`

STATUS: `FROZEN BEFORE FIXTURE REVIEW AND CLASSIFIER EXPOSURE`

FREEZE DATE: `2026-09-20`

STUDY TYPE: `PROSPECTIVE MATCHED-PAIR CHARACTERIZATION`

THIS IS A D1–D11 TEST: `NO`

RESEARCH-STATUS EFFECT AT PREREGISTRATION: `NONE`

## Purpose

Observe whether one varied design axis — explicit versus incompletely
specified aggregation/decision semantics before observation — affects one
D1–D11-blind reviewer's bounded diagnosticity classification in one matched
fixture pair.

## Preregistered design

```text
WORK ID:
PROSPECTIVE-DIAG-PROBE-01

CLASSIFIER:
1

PAIR COUNT:
1

VARIED AXIS:
1

VARIED AXIS DEFINITION:
explicit versus incompletely specified aggregation/decision semantics
before observation
```

All other fixture dimensions are required to match mechanically before the
pair may be sent to the classifier.

## Preregistered epistemic limits

```text
SIGNAL: POSSIBLE
SENSITIVITY: NOT ESTIMATED
SPECIFICITY: NOT ESTIMATED
GENERALIZATION: NOT ESTABLISHED
METHOD VALIDATION: NOT ESTABLISHED
```

## Predicted semantic direction

The case with explicit aggregation/decision semantics is predicted to receive
a less adverse bounded diagnosticity classification than the otherwise
matched case with incompletely specified aggregation/decision semantics.

For this single-pair characterization, classification direction is ordered
only for applying the preregistered result rule:

```text
DIAGNOSTIC
above UNRESOLVED
above NON-DIAGNOSTIC
```

This ordering is not a general measurement scale and does not assign a
numerical effect size.

The prediction and case-to-axis mapping must not be included in the blind
classifier package.

## Preregistered result rules

```text
X/Y differ in classification in predicted semantic direction:
-> evidence that the varied axis can affect this reviewer's
   bounded diagnosticity classification in this fixture.

both DIAGNOSTIC:
-> varied axis not shown necessary for this reviewer's
   bounded classification in this fixture.

both UNRESOLVED:
-> fixture may not discriminate or another requirement may dominate.

both NON-DIAGNOSTIC:
-> possible fixture defect or another dominant factor;
   do not infer the varied axis caused the result.
```

If classifications differ opposite to the predicted semantic direction, the
result is preserved as an unexpected result. It is not converted to support
for the prediction.

## Non-claims

No result from this one-classifier, one-pair probe may establish or estimate:

- sensitivity;
- specificity;
- general method validity;
- general D9 necessity;
- generalization beyond this reviewer and fixture pair;
- validation of any existing method;
- a change to any historical result or research status.

## Required pre-classifier sequence

1. Receive the original Sonnet fixture output.
2. Freeze its exact bytes and compute SHA-256.
3. Perform only the preregistered mechanical matched-pair audit.
4. Freeze the audit result and compute SHA-256.
5. If and only if all six required checks are `YES`, build a blind package
   containing only CASE X, CASE Y and the frozen classifier instruction.
6. Freeze the exact blind package and its file hashes before classifier
   exposure.

No diagnosticity assessment is permitted during fixture verification.

## Blind-package exclusions

The classifier package must not contain:

- D1–D11;
- D9;
- F2;
- historical Step 2, CF01, localization or applicability results;
- prior classifier results;
- this preregistration;
- the varied-axis label or case-to-axis mapping;
- the predicted direction;
- any reviewer assessment of either fixture.

## Stop rules

No fixture may be improved, completed or repaired by Work. If the matched-pair
requirements are not mechanically established, the pair is not sent to the
classifier. A replacement or repair would require a separately versioned
fixture output and a new mechanical audit; this preregistration does not
authorize either action.

DF-011 is not part of this probe and is not run.

