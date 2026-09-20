# PROSPECTIVE-DIAG-PROBE-01 — D9 new-evidence mapping result

VERSION: `v0.1`

STATUS: `FROZEN AS RUN`

RUN DATE: `2026-09-20`

PLAN EXECUTED:
`D9_NEW_EVIDENCE_MAPPING_PLAN_v0.1.md`

PLAN SHA-256:
`61306c6f10f238699b7381a0c4d4e55e26625ac995a5c6cdd2e0d0ea845392a9`

PLAN MODIFIED: `NO`

D1–D11 EXECUTION: `NOT RUN`

DF-011 EXECUTION: `NOT RUN`

PATCH STATUS: `NONE`

RESEARCH-STATUS EFFECT: `BOUNDED NEW-EVIDENCE MAPPING ONLY`

## 1. Provenance precheck

The provenance-companion history was audited before this mapping and frozen
in `FRIDA_VERBATIM_SOURCE_PROVENANCE_HISTORY_v0.1.md`.

SHA-256:
`667d62464b17c2221103c3395c043891fa31e813694c19d18fa70ae65a5a09dd`

Result:

```text
9474d9b4e7437af7343935d173dfced53e7b5a88b46b6946e5446189b80c4060
= valid mechanically computed identity of the prior 940-byte revision

20d8b21d045a2b6d81ef1dddf72148185a667017db37646bd68f46d2f44a02f5
= valid mechanically computed identity of the current 1248-byte revision

HASH REPORTING ERROR:
NO

IN-PLACE FILE CHANGE:
YES
```

The prior exact bytes are no longer present and were not reconstructed. The
verbatim Frida source itself is unchanged at SHA-256
`b541eb75f68efc4b37bad9f9678ed2576fc9a23e23fd4a8fc1ebf028c51a5483`.

## 2. Frozen mapping inputs

```text
PROSPECTIVE-DIAG-PROBE-01

CASE X = DIAGNOSTIC
CASE Y = NON-DIAGNOSTIC
X ≠ Y

PRE-REGISTERED DIRECTION = OBSERVED
SIGNAL = YES

PAIR COUNT = 1
CLASSIFIER COUNT = 1
ORDER EFFECT = RECORDED, NOT CONTROLLED

SENSITIVITY = NOT ESTIMATED
SPECIFICITY = NOT ESTIMATED
GENERALIZATION = NOT ESTABLISHED
GENERAL D9 NECESSITY = NOT ESTABLISHED
```

| Input | SHA-256 |
|---|---|
| `fixtures/CASE_X.md` | `3792ee0f812928331c1ef67200d06e070d76089484dadc0aa355ccdc42888bb9` |
| `fixtures/CASE_Y.md` | `4e94deff444371dab5758689ecf985b86e0f582ea179241cc5ad73de6938b6b2` |
| `PRE_FRIDA_MECHANICAL_FIXTURE_AUDIT_RESULT_v0.1.md` | `012c371c34a0b8c103df48c3ead1ddae60b0d19d80f167e4fb0233f2e4ae3e34` |
| `PROSPECTIVE_DIAG_PROBE_01_PRIMARY_RESULT_v0.1.md` | `bb59de279ee122c91c06454a0e77c2a9dbab2dfc392fb641750300a2ed8ac51d` |
| `FRIDA_BLIND_CLASSIFICATION_VERBATIM_SOURCE_v0.1.md` | `b541eb75f68efc4b37bad9f9678ed2576fc9a23e23fd4a8fc1ebf028c51a5483` |

## 3. Component boundary

```text
D9-A = aggregation / decision semantic completeness

D9-B = replay / provenance-chain completeness
```

Evidence for one component is not propagated to the other.

## 4. D9-A mapping

```text
DOES PROSPECTIVE-DIAG-PROBE-01
PROVIDE NEW EVIDENCE FOR THIS COMPONENT?

YES
```

### Exact fixture variation

The frozen mechanical audit established that the two cases are matched before
the aggregation/decision-semantics section. The varied content is:

- CASE X fixes before observation the item aggregation rule, handling of
  INVALID and missing outputs, metric, ambiguity/tie handling and exact
  aggregate-to-conclusion rule;
- CASE Y leaves those same elements undetermined until after the 240 raw
  verdicts are observed.

No other fixture-content difference was identified by the frozen mechanical
audit.

### Exact primary observation

```text
CLASSIFICATION(X) = DIAGNOSTIC
CLASSIFICATION(Y) = NON-DIAGNOSTIC
X ≠ Y
PRE-REGISTERED DIRECTION = OBSERVED
```

This classification pair, rather than the classifier's explanation, is the
primary observation used for the D9-A answer.

### Correspondence with the previously localized semantic question

The manipulated axis is pre-observation completeness of the load-bearing
rules that map item verdicts to aggregate scores and aggregate scores to the
named decision. This is the aggregation/decision-semantic-completeness class
defined as D9-A in the frozen plan.

The earlier historical D9 localization concerned an incompletely specified
load-bearing quantitative relation and the resulting inability to complete a
determinate experiment-level mapping. The prospective manipulation therefore
corresponds to that semantic component at the component level: both concern
whether load-bearing aggregation/decision relations are fixed before the
result is interpreted.

The probe does not complete the historical phrase `mätbart bättre`, replay the
historical experiment or establish that all possible D9-A requirements are
necessary.

### Bounded conclusion

The matched classification difference supplies new evidence that
pre-observation aggregation/decision semantic completeness can affect this
classifier's bounded diagnosticity classification in this fixture pair.

Attribution remains qualified by the fixed review order, one pair and one
classifier.

### Secondary context

Frida's stated reasons identify the complete versus incomplete
observation-to-conclusion mapping as decisive. Those statements are preserved
as:

```text
SECONDARY CONTEXT
NON-DECISIVE FOR PRIMARY RESULT
```

They are consistent with the primary observation but are not used to create,
replace or upgrade it. No D1–D11 information is introduced retroactively into
her classification.

## 5. D9-B mapping

```text
DOES PROSPECTIVE-DIAG-PROBE-01
PROVIDE NEW EVIDENCE FOR THIS COMPONENT?

NO
```

### Exact fixture variation

No replay/provenance-chain axis was varied. Both cases specify the same:

- 240 verdicts and 80 generation calls;
- JSONL raw-data schema;
- append-only API-call log schema;
- scoring inputs;
- fixed checkpoint hashes, prompt-template versions, seeds and harness commit
  provenance;
- execution structure and prospective data collection.

The frozen mechanical audit found these elements identical.

### Exact primary observation

The only primary observation is the classification pair:

```text
CLASSIFICATION(X) = DIAGNOSTIC
CLASSIFICATION(Y) = NON-DIAGNOSTIC
```

Because replay/provenance completeness did not vary, this difference cannot
discriminate D9-B alternatives. The positive D9-A result is not propagated to
D9-B.

### Secondary context

Frida's descriptions of validity, representativeness, reliability and absent
raw results are secondary stated reasons and uncertainties. They do not turn
the unvaried replay/provenance dimension into a primary experimental
observation.

## 6. Combined mapping result

```text
NEW EVIDENCE FOR D9-A ONLY
```

This means only that the prospective probe adds bounded evidence for the
aggregation/decision-semantic-completeness component in this fixture and for
this classifier. It provides no new evidence for replay/provenance-chain
completeness.

## 7. Historical and method boundaries

```text
F2 HISTORICAL EVENT:
PRESERVED

WHOLE-METHOD ATTRIBUTION:
previously qualified by applicability audit
```

This mapping does not change the historical F2 event, CF01, Frida's historical
classification or the applicability audit. It addresses only what the new
prospective probe contributes to the surviving D9 question.

## 8. Prohibited upgrades

The result does not establish:

```text
D9 VALIDATED
D9 GENERALLY NECESSARY
D1–D11 VALIDATED
SENSITIVITY ESTABLISHED
SPECIFICITY ESTABLISHED
```

It also does not establish generalization, eliminate the order effect or
validate a method. No gate patch, new gate, normative primitive or DF-011 run
is introduced.
