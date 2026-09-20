# HIST-DIAG-CTRL-01 — D9 residual-carrier stoppunkt

RECORD VERSION: `v0.1`

RECORD STATUS: `FROZEN`

RECORD DATE: `2026-09-20`

RECORD TYPE: `NON-EXECUTION / STOP-POINT RECORD`

PATCH STATUS: `NONE`

RESEARCH-STATUS EFFECT: `NONE`

## 1. Preserved state

```text
HISTORICAL STEP-2 EVENT:
F2 FALSE POSITIVE / METHOD FAIL

CF01:
EPISTEMIC OUTCOME = UNRESOLVED
ACTION = HOLD

FRIDA:
DIAGNOSTIC

APPLICABILITY AUDIT:
D1 NOT ESTABLISHED
D2 NOT ESTABLISHED
D3 ESTABLISHED
D4 NOT ESTABLISHED
D5 NOT ESTABLISHED
D6 NOT ESTABLISHED
D7 ESTABLISHED
D8 ESTABLISHED
D9 ESTABLISHED
D10 ESTABLISHED
D11 ESTABLISHED
```

The states above are historical inputs to this stop-point record. None is
reassessed or changed here.

## 2. D9 residual-carrier decision

```text
D9 RESIDUAL-CARRIER STATUS:
UNRESOLVED

NEW EVIDENCE SINCE F-NOT-ADDRESSED:
NONE IDENTIFIED

D9 APPLICABILITY:
ESTABLISHED

D9 ORIGINAL STEP-2 OUTCOME:
UNRESOLVED / BLOCKING

WHETHER D9'S REQUIREMENT IS NECESSARY WITHIN
FRIDA'S FROZEN DIAGNOSTICITY BASIS:
NOT ESTABLISHED

D9 RESIDUAL-CARRIER RUN:
NOT EXECUTED

REASON:
With no new evidence, the proposed run could not discriminate between
the already known alternatives and would risk becoming
non-diagnostic by construction.
```

This record freezes the decision not to run the proposed D9 residual-carrier
analysis on the unchanged evidence set.

## 3. Attribution boundary

```text
F2 AS HISTORICAL EVENT:
PRESERVED

WHOLE D1–D11 METHOD-LEVEL ATTRIBUTION:
NOT CLEANLY ESTABLISHED

SURVIVING ESTABLISHED-APPLICABLE BLOCKER:
D9

WHETHER D9 CAN SUSTAIN THE METHOD-LEVEL ATTRIBUTION:
UNRESOLVED
```

The applicability audit established D9 applicability. It did not establish
that D9's requirement is necessary within Frida's frozen diagnosticity basis
or that D9 alone sustains the earlier whole-method attribution.

## 4. Structural finding

```text
STRUCTURAL FINDING:
The frozen D1–D11 method did not contain an explicit
applicability-resolution step sufficient to prevent
experiment-form-specific gates from being evaluated where
applicability had not been established.

REMEDY:
UNRESOLVED
```

This is a structural observation about the frozen run and method text. It is
not a patch, defect classification or new method component.

## 5. Frozen source identities

| Source | SHA-256 |
|---|---|
| `STEP_2_POSITIVE_CONTROL_HIST_DIAG_CTRL_01_RESULT_v0.1.md` | `5ac3beaac47522c9bd2fe661a20181c6c43383c8ab0aeb6bb148d6a2c74a186e` |
| `HIST_DIAG_CTRL_01_CF01_COUNTERFACTUAL_CHARACTERIZATION_v0.1.md` | `b39cc784a8be0d5223c996efd18c9d4e6d56199ce9333b32599835316672a560` |
| `FRIDA_BLIND_CLASSIFICATION_RESULT.md` | `ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2` |
| `FRIDA_BLIND_CLASSIFICATION_BASIS_ADDENDUM_v0.1.md` | `2051906083cd657c5f72acf4be25ff77a9e9ff672ab564482d2a534f3437b88f` |
| `HIST_DIAG_CTRL_01_D4_D5_D9_FAILURE_LOCALIZATION_v0.1.md` | `f05b50b2f3a897077baec9ef5e54ac3d950f4b1bac6dbf878648796593c96b13` |
| `HIST_DIAG_CTRL_01_D1_D11_APPLICABILITY_AUDIT_v0.1.md` | `446cae0ea958d12714067a58a8d29eceb1f3c707b60fa406b56007bb00639859` |

## 6. Non-actions

- no D9 residual-carrier run was performed;
- no gate was changed or added;
- no D0 or `N/A` status was introduced;
- no applicability primitive was introduced;
- no patch was proposed or applied;
- DF-011 was not run;
- no research status was changed.

