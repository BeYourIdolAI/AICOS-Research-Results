# HIST-DIAG-CTRL-01 — D4/D5/D9 failure localization

RESULT VERSION: `v0.1`

RESULT STATUS: `FROZEN AS RUN`

RUN DATE: `2026-09-20`

ANALYSIS TYPE: `FAILURE LOCALIZATION`

PATCH STATUS: `NONE`

RESEARCH-STATUS EFFECT: `NONE`

DF-011 EXECUTION: `NOT RUN`

## 1. Frozen inputs and boundaries

### Step 2

```text
F2 FALSE POSITIVE / METHOD FAIL
```

Source: `STEP_2_POSITIVE_CONTROL_HIST_DIAG_CTRL_01_RESULT_v0.1.md`

SHA-256:
`5ac3beaac47522c9bd2fe661a20181c6c43383c8ab0aeb6bb148d6a2c74a186e`

### Counterfactual CF01

```text
EPISTEMIC OUTCOME = UNRESOLVED
ACTION = HOLD
```

Source: `HIST_DIAG_CTRL_01_CF01_COUNTERFACTUAL_CHARACTERIZATION_v0.1.md`

SHA-256:
`b39cc784a8be0d5223c996efd18c9d4e6d56199ce9333b32599835316672a560`

### Frida classification

```text
CLASSIFICATION = DIAGNOSTIC
SCOPE = v3.3 Del A / testade scenarier
D1–D11 EXPOSURE = NO
```

Source: `FRIDA_BLIND_CLASSIFICATION_RESULT.md`

SHA-256:
`ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2`

### Frida classification-basis addendum

Source:
`FRIDA_BLIND_CLASSIFICATION_BASIS_ADDENDUM_v0.1.md`

SHA-256:
`2051906083cd657c5f72acf4be25ff77a9e9ff672ab564482d2a534f3437b88f`

Provenance limitation: the complete verbatim follow-up attributed to Frida was
not supplied as a separate source file. The addendum freezes the exact P1–P5
propositions and response distinctions in the supplied instruction and does
not reconstruct omitted item-level wording.

### Frozen method

Source: `AICOS_DIAGNOSTICITY_PREFLIGHT_v0.1.md`

SHA-256:
`3d925e198bba7aa712ffa4855d29f69d2d255334c1b1883255390882691b34ee`

Step 1 addendum source:
`AICOS_DIAGNOSTICITY_METHOD_PACK_v0.1_EVIDENCE_BASIS_ADDENDUM_01.md`

SHA-256:
`dd1f124bfa0e812a2a0019450b595445e13ab69d18b750397c4e98d6ad5c1301`

No gate is changed or reassessed. This run localizes only why the frozen D4,
D5 and D9 results were `UNRESOLVED`.

## 2. External reference: Frida's frozen basis

```text
P1 — verkligt diskriminerande möjliga utfall
P2 — bedömningsregler satta före resultaten
P3 — tillräckligt jämförbar MED/UTAN-execution
P4 — faktisk möjlighet till positiva, neutrala och negativa utfall
P5 — tillräcklig resultatkedja för den avgränsade Del A-frågan
```

This basis is used only to map what Frida's `DIAGNOSTIC` classification relied
on. It does not redefine D1–D11.

## 3. D4 — CONTROL VIABILITY

FROZEN GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

### 3.1 Exact unresolved proposition

Frozen gate definition:

```text
H_FULL/control must be independently conformant before attack evaluation.

If control fails for an axis-independent reason:

INVALID TRACE
or
NON-DIAGNOSTIC FIXTURE.
```

Frozen Step 2 assessment:

> The untreated comparator is operationally viable and produces useful
> answers. The frozen D4 text, however, requires `H_FULL/control` to be
> independently conformant before attack evaluation. This experiment defines
> neither H_FULL nor an independent conformance criterion for the
> no-system-prompt arm.

The exact unresolved proposition is:

```text
WHETHER THE UTAN ARM IS H_FULL/control AND IS INDEPENDENTLY CONFORMANT
UNDER A CONFORMANCE CRITERION DEFINED FOR D4 BEFORE ATTACK EVALUATION.
```

### 3.2 Exact PASS evidence requirement

D4 required all of the following without a new during-test equivalence rule:

1. an identified `H_FULL/control` arm;
2. an independently specified conformance criterion for that arm; and
3. evidence that the arm satisfied that criterion before attack evaluation.

Evidence that UTAN was operationally usable, including the observed S5
normal-case result, did not by itself establish that D4-specific proposition.

### 3.3 Mapping against Frida's frozen basis

CLASSIFICATION: `F-NOT-ADDRESSED`

P3 expressly requires sufficiently comparable MED/UTAN execution. Frida's
frozen classification also treats the comparator as usable within bounded Del
A. Her P1–P5 basis does not state that UTAN must instantiate `H_FULL/control`
or satisfy a separately defined D4 conformance contract. The relation between
ordinary comparator viability and D4 conformance is therefore not decided by
her frozen basis.

`F-NOT-ADDRESSED` is not filled by a new diagnosticity judgment.

### 3.4 Evidence location

CLASSIFICATION: `A — ABSENT FROM EXPERIMENT/DESIGN ITSELF`

Source evidence:

- `Valideringsplan_v1.md` defines UTAN as execution without a system prompt;
- the plan defines the S5 normal-case usefulness check;
- the result reports observed S5 usefulness in both arms;
- neither the plan nor the frozen Step 2 source identifies `H_FULL/control`
  or a separate independent conformance criterion for UTAN.

The missing D4 proposition is therefore absent at the design-definition
level. It is not merely an unavailable historical raw file.

### 3.5 Localized consequence

D4 requires a proposition not established by the historical design and not
resolved by Frida's P1–P5 basis. The preserved evidence supports comparator
viability and comparability, but it does not establish the frozen gate's
independent `H_FULL/control` conformance proposition.

No conclusion is drawn here about whether D4 or Frida's classification is
correct.

## 4. D5 — ATTACK-SENSITIVE BLOCKER

FROZEN GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

### 4.1 Exact unresolved proposition

Frozen gate definition:

```text
For blocker B:

B(H_CONTROL) = FALSE
B(H_ATTACK) = TRUE

TRUE / TRUE is an ORTHOGONAL BLOCKER.
FALSE / FALSE makes the blocker irrelevant.
UNRESOLVED / anything prevents determinate PASS/FAIL.
```

Frozen Step 2 assessment:

> The historical design does not define one blocker B with the frozen matrix:
> `B(H_CONTROL) = FALSE`, `B(H_ATTACK) = TRUE`. Constructing such a blocker
> from the five outcomes after execution would be a new mapping and a new
> judgment.

The exact unresolved proposition is:

```text
WHETHER A SINGLE PREDEFINED BLOCKER B HAS FALSE BEHAVIOR IN THE CONTROL ARM
AND TRUE BEHAVIOR IN THE ATTACK ARM FOR THIS HISTORICAL EXPERIMENT.
```

### 4.2 Exact PASS evidence requirement

D5 required:

1. an exact blocker `B` defined before applying the gate;
2. an exact mapping from the historical control and attack arms to
   `H_CONTROL` and `H_ATTACK`; and
3. preserved evidence establishing `B(H_CONTROL) = FALSE` and
   `B(H_ATTACK) = TRUE`.

The five scenario-specific outcomes could not be converted after execution
into this single matrix without adding a new mapping.

### 4.3 Mapping against Frida's frozen basis

CLASSIFICATION: `F-NOT-ADDRESSED`

P1 and P4 require genuinely discriminating possible outcomes and the actual
possibility of positive, neutral and negative outcomes. They do not expressly
require one blocker `B` or the frozen D5 control/attack truth matrix. Frida's
basis therefore does not decide the relation between her multi-scenario
diagnosticity judgment and this exact blocker formalism.

The Step 1 addendum independently records D5's source mapping as unresolved.
No intuitive mapping is supplied here.

### 4.4 Evidence location

CLASSIFICATION: `A — ABSENT FROM EXPERIMENT/DESIGN ITSELF`

Source evidence:

- `Valideringsplan_v1.md` defines five scenario-specific behavioral outcomes;
- the preserved report records positive, neutral and negative directions;
- neither defines one blocker `B` with the required D5 truth matrix;
- Step 1 addendum section 6 says no examined source conclusively maps the
  orthogonal-blocker pattern to an exact experiment.

The missing formal mapping is absent from the historical design rather than
merely lost from the preserved raw-output set.

### 4.5 Localized consequence

D5 requires a single blocker mapping that the historical experiment did not
define. Frida's classification relied on discriminating, multi-directional
scenario outcomes, while her frozen basis does not address whether those
outcomes must also instantiate D5's single-blocker matrix.

No conclusion is drawn here about whether D5 or Frida's classification is
correct.

## 5. D9 — SEMANTIC COMPLETENESS

FROZEN GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

### 5.1 Exact unresolved proposition

Frozen gate definition:

```text
Before PASS/FAIL, identify every load-bearing term, threshold, prerequisite
and semantic relation.

Unresolved relation in frozen text:

AMBIGUOUS.

Required but neither established nor legitimately stipulated:

INVALID TRACE.
```

Frozen Step 2 assessment:

> Not every load-bearing threshold and evidentiary relation required for a
> full experiment-level PASS/FAIL is established. In particular, `mätbart
> bättre` is not quantitatively completed and some reported
> observation-level judgments cannot be independently replayed from the
> packaged raw files.

The exact unresolved proposition is:

```text
WHETHER EVERY LOAD-BEARING THRESHOLD AND EVIDENTIARY RELATION NEEDED FOR THE
FULL EXPERIMENT-LEVEL PASS/FAIL IS BOTH SEMANTICALLY COMPLETE AND SUPPORTED BY
A REPLAYABLE PRESERVED RESULT CHAIN.
```

### 5.2 Exact PASS evidence requirement

D9 required:

1. a completed meaning for every load-bearing threshold, including the
   intended quantitative relation for `mätbart bättre`;
2. identified prerequisites and semantic relations for the assessed result;
   and
3. sufficient preserved observation-level evidence to establish the
   load-bearing result judgments without reconstructing missing material.

### 5.3 Mapping against Frida's frozen basis

CLASSIFICATION: `F-NOT-ADDRESSED`

P2 requires assessment rules set before results. P5 requires a sufficient
result chain for the bounded Del A question. These overlap with D9 but do not
answer the exact all-terms/all-relations proposition imposed by the frozen
gate.

The original classification explicitly tolerated the lack of a separate raw
file for every completed observation, the four missing runs and the
unperformed Part B while retaining bounded Del A diagnosticity. That portion
of the D9 evidence concern is therefore known and classification-tolerated.

The frozen basis does not separately decide whether the phrase `mätbart
bättre` was quantitatively complete under D9, nor whether every
experiment-level relation had to be independently replayable. Because the
gate-level requirement combines those questions, the exact D9 relation is
`F-NOT-ADDRESSED` rather than being filled from partial overlap with P2 or P5.

### 5.4 Evidence location

CLASSIFICATION: `D — CANNOT DETERMINE AS ONE SOURCE CLASS FROM CURRENT EVIDENCE`

Two established components prevent a single A/B/C allocation:

- **A component:** the plan uses `mätbart bättre` without a numerical
  difference threshold, so this semantic completion is absent from the
  experiment design itself;
- **B component:** the historical experiment may have produced additional
  observation-level support, but the preserved snapshot lacks a separate raw
  response for every completed observation and a complete replayable
  observation-level score sheet.

Current evidence cannot determine whether the absent observation-level
material never existed or existed but was not retained. No C finding is made:
the run does not establish that sufficient evidence is present but merely
unrecognized by the gate.

### 5.5 Localized consequence

D9 remains unresolved through a combination of an incomplete design-level
threshold and an incomplete preserved replay chain. Frida expressly tolerated
the raw-file and missing-run limitations for bounded Del A, while her frozen
basis does not settle the full D9 semantic-completeness proposition.

No conclusion is drawn here about whether D9 or Frida's classification is
correct.

## 6. Cross-gate result

| Observed localization | Gate/component |
|---|---|
| DESIGN INSUFFICIENCY | D4; D5; D9 threshold component |
| HISTORICAL DOCUMENTATION INSUFFICIENCY | D9 replay-chain component |
| GATE/EVIDENCE-RECOGNITION INSUFFICIENCY | none established |
| UNRESOLVED | D9 gate-level allocation remains composite; existence of additional unpreserved observation evidence cannot be determined |

The gates are not forced into one common root cause:

- D4 localizes to the absent `H_FULL/control` conformance definition;
- D5 localizes to the absent single-blocker mapping;
- D9 localizes to both a design-level semantic gap and a preservation-level
  replay gap.

## 7. What is established

- D4's frozen PASS proposition is stronger and differently formulated than
  ordinary comparator usability or MED/UTAN comparability.
- The historical design does not define the D4-specific `H_FULL/control`
  conformance contract.
- The historical design does not define D5's single blocker `B` and truth
  matrix.
- D9 contains a design-level ambiguity in `mätbart bättre`.
- D9 also encounters an incomplete preserved observation-level replay chain.
- Frida's frozen classification expressly tolerated the raw-file gap, four
  missing runs and absent Part B for bounded Del A.
- Frida's P1–P5 basis does not decide the exact D4, D5 or complete D9
  propositions.

## 8. What remains unresolved

- whether ordinary comparator viability should ever satisfy D4 conformance;
- whether D5's blocker formalism applies to a multi-scenario comparative
  experiment of this kind;
- the intended quantitative completion of `mätbart bättre`;
- whether additional observation-level raw or scoring evidence once existed;
- whether a complete Frida follow-up response contains item-level distinctions
  beyond the exact P1–P5 propositions supplied here;
- whether the frozen method would pass a separate negative control.

No missing evidence is reconstructed.

## 9. DF-011 gate

NEW TEST DIMENSION: `YES — PROSPECTIVE ARTIFACT-CONTROL DIMENSION`

The localization is mainly A for D4 and D5 and composite A/B for D9. A
prospective DF-011 probe could therefore test something not established by the
historical case: behavior of the frozen gates when the control/attack mapping,
blocker, semantic thresholds and preservation requirements are specified
before execution and preserved in a gate-usable form.

This finding does not authorize or run DF-011. It does not predict DF-011's
result. Before execution, DF-011's packet would need a separate check that it
does not reproduce the same artifact-preservation uncertainty observed in the
historical case.

DF-011 remains `NOT RUN` in this analysis.

## 10. Frozen outcome preservation

```text
ORIGINAL STEP 2 RESULT:
F2 FALSE POSITIVE / METHOD FAIL

STATUS:
UNCHANGED

CF01 EPISTEMIC OUTCOME:
UNRESOLVED

CF01 ACTION:
HOLD

STATUS:
UNCHANGED

FRIDA CLASSIFICATION:
DIAGNOSTIC

STATUS:
UNCHANGED
```

This result is a localization record only. It introduces no patch, no new
gate and no research-status change.
