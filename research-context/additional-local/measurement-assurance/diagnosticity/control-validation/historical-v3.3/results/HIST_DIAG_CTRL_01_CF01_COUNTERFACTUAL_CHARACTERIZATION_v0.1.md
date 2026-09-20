# HIST-DIAG-CTRL-01-CF01 — Counterfactual characterization

RESULT VERSION: `v0.1`

RESULT STATUS: `FROZEN AS RUN`

RUN DATE: `2026-09-20`

ANALYSIS TYPE: `COUNTERFACTUAL CHARACTERIZATION`

PATCH STATUS: `NONE`

RESEARCH-STATUS EFFECT: `NONE`

## 1. Frozen inputs

### Historical positive control

```text
CASE ID:
HIST-DIAG-CTRL-01

CLASSIFICATION:
DIAGNOSTIC

SCOPE:
v3.3 Del A / tested scenarios

CLASSIFIER EXPOSURE:
D1–D11-blind; not case-naive or fully independent
```

Frozen classification artifact SHA-256:
`ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2`

### Frozen Step 2 result

```text
OVERALL METHOD OUTCOME:
F2 FALSE POSITIVE / METHOD FAIL
```

Frozen Step 2 result SHA-256:
`5ac3beaac47522c9bd2fe661a20181c6c43383c8ab0aeb6bb148d6a2c74a186e`

This counterfactual does not modify, supersede or remove that result.

### Frozen gate outputs

```text
D1  PASS
D2  PASS
D3  PASS
D4  UNRESOLVED
D5  UNRESOLVED
D6  PASS
D7  PASS
D8  PASS
D9  UNRESOLVED
D10 PASS
D11 PASS
```

No gate is reopened or reassessed.

### Preserved source limitations

- 96/100 planned runs have data.
- Runs 079, 080, 082 and 110 remain missing.
- Missing evidence is not reconstructed.
- Part B was not performed.
- No Part B result is inferred.

## 2. Counterfactual rule

### Epistemic aggregation

```text
if any blocking gate = FAIL:
    aggregate = REJECTED

else if one or more blocking gates = UNRESOLVED:
    aggregate = UNRESOLVED

else:
    aggregate = ACCEPTED
```

```text
UNRESOLVED != REJECTED
UNRESOLVED != ACCEPTED
```

### Action policy

```text
ACCEPTED   -> ALLOW
REJECTED   -> BLOCK
UNRESOLVED -> HOLD / DO NOT ALLOW YET
```

The epistemic aggregation and the action policy are applied as separate steps.

## 3. Application to the frozen outputs

Blocking gate results:

```text
FAIL:
NONE

UNRESOLVED:
D4, D5, D9
```

The first aggregation branch is not triggered because no blocking gate is
`FAIL`.

The second aggregation branch is triggered because one or more blocking gates
are `UNRESOLVED`.

Therefore:

```text
EPISTEMIC AGGREGATE:
UNRESOLVED
```

Applying the action policy to that epistemic aggregate gives:

```text
OPERATIONAL ACTION:
HOLD / DO NOT ALLOW YET
```

`HOLD` records absence of authorization under the counterfactual policy. It is
not evidence that the historical experiment is bad or non-diagnostic.

## 4. Q1 — Epistemic effect

QUESTION:

```text
When UNRESOLVED is preserved as a distinct state,
is HIST-DIAG-CTRL-01 still REJECTED?
```

ANSWER:

```text
NO
```

EXACT REASON:

There are no frozen `FAIL` gate outputs. D4, D5 and D9 are frozen as
`UNRESOLVED`. Under the counterfactual aggregation rule, those results select
the `UNRESOLVED` branch and cannot select the `REJECTED` branch.

## 5. Q2 — Operational effect

QUESTION:

```text
Under the preregistered action policy,
would HIST-DIAG-CTRL-01 be allowed to proceed?
```

ANSWER:

```text
HOLD
```

EXACT REASON:

The action policy maps `UNRESOLVED` to `HOLD / DO NOT ALLOW YET`. It does not
map `UNRESOLVED` to either `ALLOW` or `BLOCK`.

## 6. Q3 — Outcome classification

```text
EPISTEMIC STATE:
UNRESOLVED

ACTION:
HOLD

EPISTEMIC FALSE REJECTION:
NO

OPERATIONAL GOOD-CASE NON-ADMISSION:
YES
```

## 7. Established by this counterfactual

The following is established under the preregistered counterfactual rules:

- preserving `UNRESOLVED` prevents the frozen gate outputs from becoming an
  epistemic `REJECTED` result;
- the positive control remains operationally unadmitted because the action
  policy maps `UNRESOLVED` to `HOLD`;
- epistemic classification and operational authorization produce distinct
  outputs;
- `HOLD` does not classify the experiment as bad or non-diagnostic;
- no `FAIL` exists among the frozen gate outputs.

## 8. Still unresolved

The following remains unchanged and unresolved:

- D4;
- D5;
- D9;
- the missing runs 079, 080, 082 and 110;
- the absent complete observation-level raw-file set;
- the unperformed Part B assessment;
- whether the frozen method would pass a separate negative control.

No failure localization for D4, D5 or D9 is performed here.

## 9. Chain characterization

```text
FROZEN GATE OUTPUTS:
8 PASS / 0 FAIL / 3 UNRESOLVED

COUNTERFACTUAL AGGREGATION:
UNRESOLVED

COUNTERFACTUAL ACTION POLICY:
HOLD
```

Under this counterfactual, the epistemic false-rejection consequence is
localized to the original aggregation of blocking `UNRESOLVED` outputs into a
rejection consequence. Preserving the epistemic state removes that consequence.

Operational good-case non-admission remains because unresolved gate outputs
combined with the preregistered action policy yield `HOLD`.

This characterization does not decide why D4, D5 or D9 are unresolved and does
not propose a remedy.

## 10. Original result preservation

```text
ORIGINAL FROZEN STEP 2 RESULT:
F2 FALSE POSITIVE / METHOD FAIL

STATUS AFTER THIS COUNTERFACTUAL:
UNCHANGED
```

The counterfactual result is additional characterization only. It is not a
patch, correction, replacement or appeal of the frozen Step 2 result.

DF-011 is not run in this analysis. No gate, evidence artifact or research
status is changed.
