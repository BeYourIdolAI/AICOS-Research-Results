# PROSPECTIVE-DIAG-PROBE-01 — Pre-Frida mechanical fixture audit result

VERSION: `v0.1`

STATUS: `FROZEN BEFORE CLASSIFIER EXPOSURE`

AUDIT DATE: `2026-09-20`

AUDIT TYPE: `MECHANICAL FIXTURE VERIFICATION ONLY`

DIAGNOSTICITY ASSESSMENT: `NOT PERFORMED`

## Frozen inputs

| Input | SHA-256 |
|---|---|
| `fixtures/CASE_X.md` | `3792ee0f812928331c1ef67200d06e070d76089484dadc0aa355ccdc42888bb9` |
| `fixtures/CASE_Y.md` | `4e94deff444371dab5758689ecf985b86e0f582ea179241cc5ad73de6938b6b2` |
| `SONNET_FIXTURE_FREEZE_MANIFEST_v0.1.md` | `aeebcc33766aaa0531930511759374c9ed153277dfb9b82535cbdf0a660e82c8` |
| `PRE_FRIDA_MECHANICAL_FIXTURE_AUDIT_PROTOCOL_v0.1.md` | `d917f8ed84f24c42cac43fa8a004b7314ce6986f34573724e37127e67772b2af` |

## Mechanical comparison result

After removal of only the neutral first-line labels `CASE X` and `CASE Y`, the
two fixture files are byte-identical from `WHAT IS BEING TESTED` through
`Other provenance`.

Their remaining difference begins at the section titled
`Aggregation / decision semantics` and is confined to whether aggregation and
decision semantics are fully specified before observation or left incomplete
until after observation.

### 1. Same research question?

RESULT: `YES`

Both files contain exactly:

```text
Does Model M's aggregate output quality on Task Set T reach θ = 0.75 and
exceed the Condition B baseline, as judged by Evaluator Panel E?
```

### 2. Same tested proposition?

RESULT: `YES`

Both files contain exactly the same hypothesis: Model M's aggregate quality on
Task Set T is at least θ = 0.75 and exceeds Condition B's aggregate quality.

### 3. Same possible outcomes?

RESULT: `YES`

Both files specify item-pass outcomes `PASS / FAIL / INVALID` and conclusion
outcomes `SUPPORTED / NOT SUPPORTED`.

### 4. Same named decision point?

RESULT: `YES`

Both files name the same post-collection decision about the proposition using
θ = 0.75 and comparison with Condition B after all 240 verdicts are collected.

### 5. Same execution structure?

RESULT: `YES`

Both files specify the same:

- conditions and fixed checkpoints;
- generation and evaluator models;
- G1 and J1 prompts;
- 40 tasks × 2 conditions × 3 evaluator passes;
- 240 evaluator judgments and 80 generation calls;
- temperature, context, measurement variables, raw-data schema, log schema,
  scoring inputs and provenance fields.

### 6. Only varied axis = aggregation/decision semantics?

RESULT: `YES`

The pre-axis content is byte-identical after the neutral case heading. CASE X
specifies aggregation, invalid/missing handling, the metric, ambiguity/tie
handling and the exact aggregate-to-conclusion rule before observation. CASE Y
leaves those same elements undetermined until after observation.

No other fixture-content difference was identified.

## Difference inventory

```text
INTENDED DIFFERENCE:
pre-observation completeness of aggregation/decision semantics

UNINTENDED DIFFERENCES:
NONE IDENTIFIED
```

## Release result

```text
REQUIRED YES RESULTS:
6 OF 6

PACKAGE ELIGIBILITY:
ELIGIBLE
```

## Integrity and scope

- neither fixture was modified during verification;
- no missing semantics were supplied;
- no fixture was improved;
- no classification was predicted or performed;
- D1–D11 were not applied;
- no historical result was used to score either case;
- no research status was changed;
- DF-011 was not run.
