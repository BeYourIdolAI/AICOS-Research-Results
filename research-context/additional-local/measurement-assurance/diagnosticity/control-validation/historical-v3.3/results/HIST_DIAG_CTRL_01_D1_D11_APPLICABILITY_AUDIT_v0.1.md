# HIST-DIAG-CTRL-01 — D1–D11 applicability audit

RESULT VERSION: `v0.1`

RESULT STATUS: `FROZEN AS RUN`

RUN DATE: `2026-09-20`

ANALYSIS TYPE: `MECHANICAL APPLICABILITY AUDIT`

PATCH STATUS: `NONE`

RESEARCH-STATUS EFFECT: `NONE`

DF-011 EXECUTION: `NOT RUN`

## 1. Preserved results

```text
STEP 2:
F2 FALSE POSITIVE / METHOD FAIL

CF01:
UNRESOLVED -> HOLD

FRIDA:
DIAGNOSTIC
```

All three remain unchanged. This audit does not reassess diagnosticity or any
frozen D1–D11 gate result.

## 2. Frozen sources

| Source | SHA-256 |
|---|---|
| `AICOS_DIAGNOSTICITY_PREFLIGHT_v0.1.md` | `3d925e198bba7aa712ffa4855d29f69d2d255334c1b1883255390882691b34ee` |
| `AICOS_DIAGNOSTICITY_CROSS_EXPERIMENT_REVIEW_v0.1.md` | `d724a1b5fcbc31c571ca41f6f6e4032e5741cb5a107234b109ecab6899f96400` |
| `STEP_2_POSITIVE_CONTROL_HIST_DIAG_CTRL_01_RESULT_v0.1.md` | `5ac3beaac47522c9bd2fe661a20181c6c43383c8ab0aeb6bb148d6a2c74a186e` |
| `FRIDA_BLIND_CLASSIFICATION_RESULT.md` | `ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2` |
| `Valideringsplan_v1.md` | `40f5c40b0fdcf700e4d61fd799ae1d293fb6d988c926e26f4d91fcaa690d1fbb` |

## 3. Mechanical object-type boundary

The historical plan defines:

```text
PURPOSE:
measure whether the Council produces a measurable effect compared with the
same model without the Council

CONDITIONS:
MED = role file + Council Operating Protocol as system prompt
UTAN = same question with no system prompt

SCENARIO STRUCTURE:
S1–S4 contain a tempting error or trap the protocol is intended to prevent
S5 intentionally contains no trap
```

It does not label either experimental condition `H_CONTROL`, `H_ATTACK` or
`H_FULL`. It does not label the Council package an `attack variable`. It does
not define one blocker `B` over those two conditions.

The following distinction is therefore preserved throughout this audit:

```text
TWO EXPERIMENTAL CONDITIONS
!=
ATTACK/CONTROL FIXTURE
```

The MED/UTAN conditions are not automatically mapped to H_ATTACK/H_CONTROL.

## 4. Gate-by-gate applicability

### D1 — SAME TARGET

Exact antecedent/object language:

```text
Control and attack arms must attempt the same proposition and epistemic status.
```

Required object types: `control arm`, `attack arm`.

Historical correspondence:

- MED and UTAN are explicitly two treatment conditions using the same model
  and question;
- the plan does not define MED as an attack arm or UTAN as a control arm in
  the method-pack sense;
- the scenario trap is held present within both conditions rather than being
  the varied MED/UTAN factor.

RESULT: `APPLICABILITY NOT ESTABLISHED`

The same-target comparison is mechanically possible across MED/UTAN, but the
frozen D1 antecedent is expressly an attack/control-arm relation. Functional
equivalence between those object types is not established by the historical
plan.

### D2 — SINGLE AXIS

Exact antecedent/object language:

```text
Only the attack variable may differ.
```

Required object type: `attack variable` varied between the relevant arms.

Historical correspondence:

- the varied MED/UTAN factor is presence of the combined Council package;
- the scenario-specific trap is present in the same prompt under both MED and
  UTAN for S1–S4;
- the plan does not define Council-package presence as an attack variable.

RESULT: `APPLICABILITY NOT ESTABLISHED`

The historical study establishes a treatment variable. It does not establish
that this variable has the same functional meaning as D2's attack variable.

### D3 — EXPLICIT DEPENDENCY

Exact antecedent/object language:

```text
Every load-bearing dependency must be established by frozen text or declared
as a fixture fact.
```

Attack-specific object language: none. The gate requires load-bearing
dependencies, frozen text and fixture facts.

Historical correspondence:

- the plan, role files and Council protocol supply frozen design dependencies;
- scenario prompts and predefined correct/incorrect behaviors supply fixture
  facts and expected relations.

RESULT: `APPLICABILITY ESTABLISHED`

### D4 — CONTROL VIABILITY

Exact antecedent/object language:

```text
H_FULL/control must be independently conformant before attack evaluation.

If control fails for an axis-independent reason:
INVALID TRACE
or
NON-DIAGNOSTIC FIXTURE.
```

Required object types: `H_FULL/control`, independent conformance and `attack
evaluation`.

Historical correspondence:

- UTAN is an untreated comparator and was operationally viable in observed
  S5 results;
- the historical design defines neither `H_FULL` nor an independent
  conformance contract for UTAN;
- the plan does not identify the MED/UTAN comparison as an attack evaluation.

RESULT: `APPLICABILITY NOT ESTABLISHED`

Comparator viability does not mechanically establish the antecedent object
`H_FULL/control` with the same functional meaning.

### D5 — ATTACK-SENSITIVE BLOCKER

Exact antecedent/object language:

```text
For blocker B:

B(H_CONTROL) = FALSE
B(H_ATTACK) = TRUE
```

Required object types: blocker `B`, `H_CONTROL`, `H_ATTACK` and a truth-valued
blocker mapping across those hypotheses/arms.

Historical correspondence:

- the plan defines five scenario-specific right/wrong behaviors;
- it does not define one blocker `B`;
- it does not define `H_CONTROL` or `H_ATTACK`;
- it does not map MED/UTAN to those objects.

RESULT: `APPLICABILITY NOT ESTABLISHED`

### D6 — NON-TAUTOLOGICAL DISCRIMINATION

Exact antecedent/object language:

```text
The varied attack variable must not be identical to the blocker's antecedent,
the rule's acceptance predicate or the exact condition named by the rule.

If the arms are defined by the rule antecedent:
NON-DIAGNOSTIC BY CONSTRUCTION.
```

Required object types: varied `attack variable`, blocker antecedent, rule
acceptance predicate and arms defined relative to those objects.

Historical correspondence:

- Council-package presence is the varied treatment;
- scenario traps are held constant across MED and UTAN within a scenario;
- no single blocker antecedent or rule acceptance predicate is defined for
  the cross-arm experiment;
- no source establishes Council-package presence as the attack variable.

RESULT: `APPLICABILITY NOT ESTABLISHED`

### D7 — NO CONCLUSION STIPULATION

Exact antecedent/object language:

```text
Fixture facts may stipulate world state, identities, timing, boundaries and
controlled inputs.

They may not stipulate attack success, attack failure, blocker outcome or the
proposition whose discovery is the result.
```

Required object types: fixture facts and an outcome proposition. The gate also
names `attack success`, `attack failure` and `blocker outcome` as prohibited
stipulations.

Historical correspondence:

- S1–S4 explicitly define traps intended to elicit tempting errors;
- each scenario defines controlled input and alternative correct/incorrect
  behavior before execution;
- the plan does not stipulate the observed outcome;
- this functional conclusion-stipulation check does not require mapping MED
  to H_ATTACK or UTAN to H_CONTROL.

RESULT: `APPLICABILITY ESTABLISHED`

This result establishes applicability of the no-conclusion-stipulation check.
It does not establish an H_ATTACK/H_CONTROL mapping.

### D8 — TYPE PRESERVATION

Exact antecedent/object language:

```text
CLAIM != EVIDENCE != ASSESSMENT != METADATA
```

Attack-specific object language: none.

Historical correspondence:

- the snapshot contains claims, preserved responses/evidence, assessments,
  logs and metadata as distinguishable artifact types.

RESULT: `APPLICABILITY ESTABLISHED`

### D9 — SEMANTIC COMPLETENESS

Exact antecedent/object language:

```text
Before PASS/FAIL, identify every load-bearing term, threshold, prerequisite and
semantic relation.
```

Attack-specific object language: none.

Historical correspondence:

- the historical plan contains terms, numerical thresholds, the phrase
  `mätbart bättre`, prerequisites and result relations used for PASS/FAIL.

RESULT: `APPLICABILITY ESTABLISHED`

This applicability result does not resolve the frozen D9 evidence gaps.

### D10 — OUTCOME-LAYER SEPARATION

Exact antecedent/object language:

```text
Keep distinct:
- NORMATIVE CONFORMANCE
- VERIFIABILITY / DETECTABILITY
- RUNTIME PREVENTION / ENFORCEMENT
```

Attack-specific object language: none.

Historical correspondence:

- the plan and results evaluate observed runtime behavior under Council rules;
- the frozen claim boundary distinguishes those observations from broader
  normative conformance and general enforcement claims.

RESULT: `APPLICABILITY ESTABLISHED`

### D11 — FALSIFIABILITY CHECK

Exact antecedent/object language:

```text
Before execution, identify a fixture-consistent world producing a different
result.
```

Attack-specific object language: none. Required object types are a fixture and
an alternative fixture-consistent result.

Historical correspondence:

- the plan defines scenario inputs and alternative correct/incorrect behavior
  before execution;
- observed results include positive, neutral and negative directions.

RESULT: `APPLICABILITY ESTABLISHED`

## 5. Applicability table

| Gate | Result |
|---|---|
| D1 | `APPLICABILITY NOT ESTABLISHED` |
| D2 | `APPLICABILITY NOT ESTABLISHED` |
| D3 | `APPLICABILITY ESTABLISHED` |
| D4 | `APPLICABILITY NOT ESTABLISHED` |
| D5 | `APPLICABILITY NOT ESTABLISHED` |
| D6 | `APPLICABILITY NOT ESTABLISHED` |
| D7 | `APPLICABILITY ESTABLISHED` |
| D8 | `APPLICABILITY ESTABLISHED` |
| D9 | `APPLICABILITY ESTABLISHED` |
| D10 | `APPLICABILITY ESTABLISHED` |
| D11 | `APPLICABILITY ESTABLISHED` |

No `N/A` gate status is introduced.

## 6. Step 2 mapping audit

### UTAN -> control

EXPLICIT EQUALITY STATEMENT: `NONE LOCATED`

IMPLICIT MAPPING: `YES`

Exact evidence:

- D4 lists UTAN/no-system-prompt evidence under `CONTROL VIABILITY`;
- D4 calls UTAN the “untreated comparator” and then applies the frozen
  `H_FULL/control` requirement to it;
- the assessment itself concedes that the experiment defines neither H_FULL
  nor an independent conformance criterion for the no-system-prompt arm.

The mapping was operationally used but not established as object-type
equivalence.

### MED -> attack

EXPLICIT EQUALITY STATEMENT: `NONE LOCATED`

IMPLICIT MAPPING: `YES`

Exact evidence:

- D1 applies a control/attack-arm gate to the MED/UTAN pair and calls them
  “arms” without separately defining the attack arm;
- D2 applies the attack-variable gate to the Council-package difference;
- D4 treats UTAN as the comparator/control-side candidate, leaving MED in the
  complementary attack-side slot for the applied gate structure.

No preserved Step 2 statement explicitly says `MED = H_ATTACK`.

### Council intervention -> attack variable

EXPLICIT EQUALITY STATEMENT: `NONE LOCATED`

IMPLICIT MAPPING: `YES`

Exact evidence:

- D2 states that the frozen comparison treats presence of the combined
  Council package as the single varied factor while applying `SINGLE AXIS`,
  whose exact antecedent says only the attack variable may differ;
- D6 substitutes “presence of the Council package” into the varied-factor
  analysis while applying `NON-TAUTOLOGICAL DISCRIMINATION`, whose exact
  antecedent is the varied attack variable.

The historical plan calls the package the MED condition/intervention whose
effect is measured. It does not call it an attack variable. The scenario trap,
not the Council package, is the object intended to tempt an error, and that
trap is held constant across MED and UTAN within each scenario.

## 7. Scope and operational applicability

Method scope header:

```text
SCOPE:
Measurement Assurance / Night Lab experiment design
```

Purpose:

```text
whether a fixture is actually diagnostic of the attack variable
```

Frozen claim boundary:

```text
the method generalizes outside this experiment family — NOT ESTABLISHED
```

FINDING:

```text
OPERATIONAL GATE APPLICABILITY IS NARROWER THAN THE SCOPE HEADER.
```

D1, D2, D4, D5 and D6 require attack-fixture objects whose corresponding
functional objects are not established in v3.3 Del A. D3 and D7–D11 have
operational formulations that can be applied without equating MED/UTAN to
H_ATTACK/H_CONTROL.

This mismatch is reported as an applicability boundary. It is not classified
as a method defect.

## 8. Characterization finding

```text
F2 was triggered in a run that applied attack-fixture-specific gates,
including D4 and D5, to a diagnostic experiment of a structurally different
MED/UTAN treatment-comparison type.

GENERALIZATION OF THE ATTACK-FIXTURE-SPECIFIC D1–D11 COMPONENTS TO THAT TYPE
WAS NOT ESTABLISHED BY THE ORIGINAL METHOD PACK.
```

This does not remove or revise F2. D9 was also a frozen blocking
`UNRESOLVED` result and its applicability to v3.3 Del A is established here.
The audit therefore does not claim that object-type applicability alone
accounts for the complete Step 2 outcome.

## 9. Preserved boundaries

- no gate was changed;
- no gate result was reassessed;
- no `N/A` status or applicability primitive was added to the method;
- no patch is proposed;
- DF-011 was not run;
- no research status was changed;
- `F2 FALSE POSITIVE / METHOD FAIL` remains unchanged;
- `CF01 UNRESOLVED -> HOLD` remains unchanged;
- Frida's `DIAGNOSTIC` classification remains unchanged.
