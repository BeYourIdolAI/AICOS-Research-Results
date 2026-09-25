# AICOS PRE-FREEZE EXPERIMENT QUALIFICATION RULE v0.1

## STATUS

```text
STATUS = FROZEN EXPERIMENT-OPERATIONS RULE
NORMATIVE AICOS CORE STATUS = NONE
RETROACTIVE EFFECT = NONE
```

## PURPOSE

This operations rule governs preparation for future confirmatory freezes. It requires evidence that the measurement pipeline works and the positive/control path is viable, with qualification criteria and a bounded shakedown effort defined in advance. Technical execution alone does not establish control viability.

Preserved parser/extraction failures, invalid controls, Diagnosticity F2, the 2ARM control failure, and R3/R3.1 positive-control failures motivated the rule. They retain their historical classifications. Their common cause is not established.

## EXPERIMENT LIFECYCLE

```text
DRAFT
↓
SHAKEDOWN
↓
QUALIFIED
↓
FROZEN
↓
EXECUTED
↓
RESULT
```

- **DRAFT** = design still under construction.
- **SHAKEDOWN** = technical and procedural development testing is allowed; implementation may change.
- **QUALIFIED** = predefined qualification criteria have been met within predefined shakedown limits.
- **FROZEN** = exact confirmatory design is locked before relevant confirmatory observation.
- **EXECUTED** = frozen confirmatory experiment has been run.
- **RESULT** = assessment produced using the frozen rules.

## RULE 1 — DEFINE QUALIFICATION CRITERIA BEFORE SHAKEDOWN

Before the first shakedown run, record the criteria for qualification. Depending on the design, these may include: parser acceptance of 10/10 representative outputs; RAW ↔ LOG identity for 10/10 attempts; correct handling of expected runtime framing; a positive control reaching its predefined required state; and mechanical distinguishability of the negative/control contrast.

These are examples, not universal thresholds. The chosen criteria and their denominators must be written before shakedown. They may not be rewritten after observing shakedown outcomes merely to obtain `QUALIFIED` status.

## RULE 2 — DEFINE SHAKEDOWN BUDGET BEFORE SHAKEDOWN

Before the first shakedown run, record the maximum number of runs or attempts, the maximum number of repair cycles, and an explicit stop or redesign condition. If the budget is exhausted without qualification, STOP or REDESIGN. Do not continue indefinite tuning or freeze merely because rebuilding is expensive.

## RULE 3 — RUN SHAKEDOWN

During SHAKEDOWN, implementation, parsers, extractors, prompts, and development fixtures may change. Log every run and every change. Preserve every failed run and its outcome.

```text
Development fixtures must be separate from the confirmatory corpus.
If a fixture is reused, that is declared as a deviation before freeze.
```

Shakedown observations must not silently become confirmatory data. If a control fixture also appears in the eventual confirmatory test, declare that reuse before freeze and record it as a deviation and contamination risk.

## RULE 4 — QUALIFICATION DECISION

```text
QUALIFIED
only if
the predefined qualification criteria are met
within the predefined shakedown budget.
```

Do not infer qualification from convenience, cost, or partial success. Do not apply post-hoc criteria. An unverified criterion cannot be counted as met.

## RULE 5 — IF NOT QUALIFIED

If the qualification criteria are not met, status remains DRAFT or SHAKEDOWN. STOP or REDESIGN, preserve all failed attempts, and do not proceed to a confirmatory freeze. A redesign requires its own criteria and bounded shakedown before qualification can be assessed again.

## RULE 6 — IF QUALIFIED, FREEZE THE CONFIRMATORY OBJECT

Before confirmatory execution, freeze at minimum: the exact confirmatory design; parser; extraction logic; runtime, model, and configuration; scoring logic; conclusion rules; control viability rule; untouched confirmatory corpus; and the manifests and hashes required to establish identity.

The confirmatory corpus must not have been used during shakedown unless reuse was declared as a deviation before freeze. Qualification does not convert shakedown observations into confirmatory evidence.

## RULE 7 — EXECUTE WITHOUT TUNING

After relevant confirmatory observation begins, do not tune the parser, extractor, scoring or conclusion rule; change a control threshold; replace a fixture; or silently substitute a corpus.

If a fatal problem is discovered, preserve the execution as failed, invalid, or stopped according to the frozen rules. Repair requires a new version and a new freeze before another confirmatory execution.

## REQUIRED INVARIANTS

```text
SHAKEDOWN SUCCESS
!=
CONFIRMATORY RESULT
```

```text
QUALIFIED
!=
GUARANTEED TO PASS
```

```text
DEVELOPMENT VALIDATION
!=
CONFIRMATORY EVIDENCE
```

```text
TRACE INTEGRITY PASS
!=
EXPERIMENTAL VALIDITY
```

```text
TECHNICAL EXECUTION SUCCESS
!=
CONTROL VIABILITY
```

## PRE-FREEZE CONTROL QUESTION

Before every future confirmatory freeze, explicitly answer:

> Are the qualification criteria predefined, the shakedown budget predefined, and the measurement pipeline plus control path actually qualified?

```text
IF any answer = NO
THEN status remains DRAFT / SHAKEDOWN
AND confirmatory freeze is not permitted.
```

An answer requires a recorded basis. Missing evidence cannot be treated as YES.

## PROVENANCE / MOTIVATION NOTE

This rule was motivated by preserved development history: Diagnosticity method/control problems; parser/extraction failures in prospective 2ARM execution; the 2ARM invalid control; R3 C1 control failure; and R3.1 repeated positive-control blockage. These are distinct historical results. This rule does not establish a shared mechanism or reclassify any of them.

```text
MOTIVATING CROSS-TRACK PATTERN
= repeated cost from freezing before technical/control qualification

COMMON CAUSE
= NOT ESTABLISHED
```

## HISTORICAL NON-RETROACTIVITY

```text
This rule does not reclassify:
F2,
EXECUTION_003,
EXECUTION_004,
EXECUTION_005,
R3,
R3.1,
or any earlier result.

Historical outcomes retain their original status.
```

## FINAL STATUS BLOCK

```text
PRE_FREEZE_QUALIFICATION_RULE = FROZEN
ROLE = EXPERIMENT_OPERATIONS
NORMATIVE_AICOS_CORE_STATUS = NONE
RETROACTIVE_EFFECT = NONE

REQUIRES_PREDEFINED_QUALIFICATION_CRITERIA = YES
REQUIRES_PREDEFINED_SHAKEDOWN_BUDGET = YES
REQUIRES_SEPARATE_DEVELOPMENT_FIXTURES = YES
CONFIRMATORY_CORPUS_REUSE_ALLOWED_ONLY_IF_PREDECLARED_AS_DEVIATION = YES

MEASUREMENT_PIPELINE_QUALIFICATION_REQUIRED = YES
CONTROL_PATH_QUALIFICATION_REQUIRED = YES

POST_OBSERVATION_TUNING_ALLOWED = NO
FAILED_SHAKEDOWN_PRESERVATION_REQUIRED = YES
```
