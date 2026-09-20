# PROSPECTIVE-DIAG-PROBE-01 — Preregistration clarification 01

VERSION: `v0.1`

STATUS: `FROZEN BEFORE CLASSIFIER RESPONSE`

FREEZE DATE: `2026-09-20`

CLASSIFIER RESPONSE OBSERVED: `NO`

PACKAGE INCLUSION: `CONTROLLER-ONLY / NOT INCLUDED IN BLIND PACKAGE`

This record adds two preregistered clarifications. It does not change the
fixtures, blind instruction or previously preregistered result rules.

## 1. Fixture identity and review order

```text
CASE X:
EXPLICIT AGGREGATION/DECISION SEMANTICS CASE

CASE Y:
INCOMPLETE AGGREGATION/DECISION SEMANTICS CASE
```

```text
REVIEW ORDER:
CASE X first
CASE Y second

ORDER EFFECT:
RECORDED, NOT CONTROLLED
```

Because this probe has one pair and one classifier, any observed X/Y
classification difference cannot be attributed to the varied axis alone
without reservation for a possible order effect.

## 2. Primary observable

```text
PRIMARY OBSERVABLE:
classification pair

i.e.
CLASSIFICATION(X), CLASSIFICATION(Y)
```

The primary result records whether:

```text
X = Y
```

or:

```text
X ≠ Y
```

and records the direction of the classification pair under the already frozen
result rules.

The classifier's stated reasons, self-rating, explanation of missingness and
statement about what the classifier believes changed the classification are
recorded as:

```text
SECONDARY CONTEXT
NON-DECISIVE FOR PRIMARY RESULT
```

They must not be used to reclassify a null result or rescue a departure from
the preregistered primary observable.

```text
SELF-REPORTED REASONING
≠
PRIMARY OBSERVATION
```

## Preserved boundaries

- fixture bytes remain unchanged;
- blind-instruction bytes remain unchanged;
- the blind-package contents remain unchanged;
- the preregistered result rules remain unchanged;
- no classifier response is observed or inferred;
- no research status is changed;
- no D1–D11 or DF-011 run is performed.
