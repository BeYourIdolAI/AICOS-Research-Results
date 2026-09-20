# AICOS Diagnosticity Step 2 — Positive-control result

CASE ID: `HIST-DIAG-CTRL-01`

RESULT VERSION: `v0.1`

RESULT STATUS: `FROZEN AS RUN`

RUN DATE: `2026-09-20`

METHOD STATUS: `CANDIDATE / NON-NORMATIVE / NOT FROZEN / NOT INDEPENDENTLY VALIDATED`

## 1. Frozen inputs

### Positive-control classification

The classification was completed before this D1–D11 run.

```text
CLASSIFICATION:
DIAGNOSTIC

SCOPE:
v3.3 Valideringsplan v1 — Del A

CONFIDENCE:
MEDIUM-HIGH
```

Classifier boundary:

```text
D1–D11-BLIND:
YES

CASE-NAIVE / FULLY INDEPENDENT:
NO
```

Frozen classification artifact:
`FRIDA_BLIND_CLASSIFICATION_RESULT.md`

SHA-256:
`ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2`

### Historical source object

Repository snapshot commit:
`a9e27559c9548522d3def2e1843a1ccf79efa4f2`

Offline source-package SHA-256:
`13983689d7fe819eeb7b6b446466112603981ac8dddf43e640d9e5cc04f0a10a`

Preserved limitations:

- 96/100 planned runs have data;
- runs 079, 080, 082 and 110 are missing;
- missing runs are not reconstructed;
- the complete observation-level raw-file set is not present;
- Part B was never performed;
- no Part B result is inferred.

### Frozen method objects

`AICOS_DIAGNOSTICITY_PREFLIGHT_v0.1.md`

SHA-256:
`3d925e198bba7aa712ffa4855d29f69d2d255334c1b1883255390882691b34ee`

`AICOS_DIAGNOSTICITY_METHOD_PACK_v0.1_EVIDENCE_BASIS_ADDENDUM_01.md`

SHA-256:
`dd1f124bfa0e812a2a0019450b595445e13ab69d18b750397c4e98d6ad5c1301`

No gate text is modified or supplemented in this run.

## 2. Preregistered result rule

```text
If the frozen D1–D11 method rejects the D1–D11-blind-classified
diagnostic control case:
F2 FALSE POSITIVE / METHOD FAIL

If the control case is not rejected:
POSITIVE-CONTROL ACCEPTANCE OBSERVED

UNRESOLVED must not be converted to PASS.
```

For this positive-control run, a dispositive frozen-method STOP prevents
acceptance. It is therefore a rejection for the preregistered acceptance test,
even where the individual gate result is `UNRESOLVED` rather than `FAIL`.

## 3. DESIGN

### D1 — SAME TARGET

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:8` fixes the same model.
- `original/validering/Valideringsplan_v1.md:9` defines MED as role file plus
  Council Operating Protocol and UTAN as the same question without a system
  prompt.
- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` fixes one prompt,
  target behavior and alternative outcomes for each scenario.

ASSESSMENT:

Within each scenario, MED and UTAN attempt the same response task and the same
behavioral proposition. The epistemic target is not changed between arms.

### D2 — SINGLE AXIS

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK AT PACKAGE LEVEL`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:8-9` fixes the model and defines
  the varied intervention as the Council package.
- `original/validering/Valideringsplan_v1.md:15` prohibits role-file or
  protocol changes during the run.
- `original/validering/validering/logg.md:5` records the manual/API deviation
  for original S4 MED.
- `original/validering/validering/logg.md:11-20,31-40` records replacement of
  manual runs 001–010 by API reruns 041–050.

ASSESSMENT:

The frozen comparison treats presence of the combined Council package as the
single varied factor. This supports only package-level attribution. It does not
support attribution to one role-file rule or to the protocol alone.

The original S4 execution-mode difference is not used as the final S4
comparison because the log identifies API reruns 041–050.

### D3 — EXPLICIT DEPENDENCY

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK FOR DESIGN DEPENDENCIES`

SOURCE EVIDENCE:

- `original/Council_Operating_Protocol.md:172,201` states that sources,
  figures and statistics must not be invented.
- `original/Forskning_och_Analyschef.md:15-16,28,54,74` supplies source,
  routing and traceability rules used by S1 and S4.
- `original/Ekonomi_och_Juridikansvarig.md:4,7-8,24,27,97` supplies the
  calculation and no-advice dependencies used by S2 and S5.
- `original/Kritisk_Granskare.md:17,21,25,72` supplies the review dependencies
  used by S3.
- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` connects each
  scenario to its predefined correct and incorrect behavior.

ASSESSMENT:

The load-bearing design dependencies are available as frozen TEXT and are not
introduced as post-result fixture conclusions.

OBSERVATION:

This gate result does not establish a complete observation-level result trace;
that evidence limitation is assessed under D8 and D9.

### D4 — CONTROL VIABILITY

GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:9` defines UTAN as no system
  prompt.
- `original/validering/Valideringsplan_v1.md:61` defines S5 as a normal-case
  usefulness check.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:14`
  reports 7/7 correct for both MED and UTAN in observed S5 data.

ASSESSMENT:

The untreated comparator is operationally viable and produces useful answers.
The frozen D4 text, however, requires `H_FULL/control` to be independently
conformant before attack evaluation. This experiment defines neither H_FULL
nor an independent conformance criterion for the no-system-prompt arm.

Treating ordinary comparator viability as equivalent to frozen D4 conformance
would add a new rule during the test. The gate therefore remains `UNRESOLVED`.

## 4. EXECUTION

### D5 — ATTACK-SENSITIVE BLOCKER

GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` defines five
  scenario-specific behavioral outcomes.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:11-15`
  records positive, neutral and negative directions across those scenarios.
- Step 1 addendum section 6 records D5 source mapping as unresolved and forbids
  intuitive source assignment.

ASSESSMENT:

The historical design does not define one blocker B with the frozen matrix:

```text
B(H_CONTROL) = FALSE
B(H_ATTACK) = TRUE
```

Constructing such a blocker from the five outcomes after execution would be a
new mapping and a new judgment. Per the frozen D5 text, unresolved blocker
behavior prevents determinate PASS/FAIL. The gate remains `UNRESOLVED`.

### D6 — NON-TAUTOLOGICAL DISCRIMINATION

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` permits success
  and failure outcomes under either arm.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:11-15`
  records different directions: MED advantages, equality and a MED failure.

ASSESSMENT:

Presence of the Council package is not identical to the acceptance predicate
or to a scored outcome. The varied factor did not guarantee one result.

### D7 — NO CONCLUSION STIPULATION

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` stipulates the
  prompts and scoring alternatives, not the observed arm outcomes.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:15`
  records an adverse S1 result for MED.

ASSESSMENT:

The fixture does not stipulate package success, package failure or the final
cross-scenario result.

## 5. ANALYSIS

### D8 — TYPE PRESERVATION

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK; MISSINGNESS REMAINS AN OBSERVATION`

SOURCE EVIDENCE:

- Snapshot structure separates `RAW`, `RESULTS`, `REPORTS`, the run log and
  the preregistered plan.
- `original/REPO_CORRECTIONS.md:10-15` records corrected counts separately.
- `original/validering/validering/logg.md:59-60,62,90` preserves the four
  missing measurements as missing.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:136-144`
  distinguishes completed observations, missing runs, unperformed Part B and
  the lack of web search.

ASSESSMENT:

The record does not relabel missing observations as evidence or Part B as a
completed assessment. Logs, results, reports and preserved responses retain
their stated artifact roles.

This `PASS` does not supply absent raw outputs and does not cure D9.

### D9 — SEMANTIC COMPLETENESS

GATE RESULT: `UNRESOLVED`

ROLE: `DISPOSITIVE / BLOCKING STOP`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:80` fixes a 90% threshold for
  listed measures.
- `original/validering/Valideringsplan_v1.md:81` additionally requires MED to
  be `mätbart bättre` than UTAN without a numerical difference threshold.
- `original/validering/validering/logg.md:59-60,62,90` records missing runs
  079, 080, 082 and 110.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:136-144`
  records 96/100 data, unperformed Part B and no web search.
- The offline snapshot does not contain a separate raw response file for every
  completed observation or a complete observation-level mechanical score
  sheet.

ASSESSMENT:

Not every load-bearing threshold and evidentiary relation required for a full
experiment-level PASS/FAIL is established. In particular, `mätbart bättre` is
not quantitatively completed and some reported observation-level judgments
cannot be independently replayed from the packaged raw files.

Per frozen D9, unresolved load-bearing semantics prevent determinate PASS/FAIL.
The gate remains `UNRESOLVED`; the missing evidence is not reconstructed.

### D10 — OUTCOME-LAYER SEPARATION

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK WITHIN THE FROZEN CONTROL CLAIM`

SOURCE EVIDENCE:

- `FRIDA_BLIND_CLASSIFICATION_RESULT.md` limits the supported result to
  observed Del A behavior within the tested scenarios and model.
- The same result explicitly excludes general effectiveness, general
  fabrication prevention, component-level causation, cross-model
  generalization and unperformed Part B claims.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:136-144`
  retains execution and evidence limitations.

ASSESSMENT:

The frozen positive-control claim concerns observed runtime behavior. It is not
promoted to general normative conformance, detectability or runtime
enforcement.

### D11 — FALSIFIABILITY CHECK

GATE RESULT: `PASS`

ROLE: `DISPOSITIVE GATE — NO BLOCK`

SOURCE EVIDENCE:

- `original/validering/Valideringsplan_v1.md:27,35,45,53,61` defines
  fixture-consistent correct and incorrect outcomes before execution.
- `original/validering/Valideringsplan_v1.md:80-82` permits failure if frozen
  thresholds or usefulness constraints are not met.
- `original/validering/validering/SLUTRAPPORT_valideringsplan_v1.md:11-15`
  contains positive, neutral and negative scenario outcomes.

ASSESSMENT:

A fixture-consistent different result existed before execution and occurred in
the preserved record. The conclusion was falsifiable.

## 6. Gate table

| Gate | Layer | Result | Disposition |
|---|---|---|---|
| D1 | DESIGN | PASS | Dispositive; no block |
| D2 | DESIGN / EXECUTION | PASS | Dispositive; package-level only |
| D3 | DESIGN | PASS | Dispositive; no design-dependency block |
| D4 | DESIGN / EXECUTION | UNRESOLVED | Blocking STOP |
| D5 | EXECUTION / ANALYSIS | UNRESOLVED | Blocking STOP |
| D6 | DESIGN | PASS | Dispositive; no block |
| D7 | DESIGN | PASS | Dispositive; no block |
| D8 | ANALYSIS | PASS | Dispositive; missingness preserved |
| D9 | ANALYSIS | UNRESOLVED | Blocking STOP |
| D10 | ANALYSIS | PASS | Dispositive within narrow claim |
| D11 | DESIGN | PASS | Dispositive; no block |

PASS: `8`

FAIL: `0`

UNRESOLVED: `3`

## 7. OVERALL METHOD OUTCOME

The frozen method does not accept the positive control because D4, D5 and D9
remain dispositive `UNRESOLVED` stops. They are not converted to PASS.

Per the preregistered Step 2 result rule:

```text
OVERALL METHOD OUTCOME:
F2 FALSE POSITIVE / METHOD FAIL
```

Interpretation boundary:

```text
FRIDA'S FROZEN CLASSIFICATION:
DIAGNOSTIC WITHIN v3.3 DEL A / TESTED-SCENARIO SCOPE

D1–D11 POSITIVE-CONTROL ACCEPTANCE:
NOT OBSERVED

D1–D11 VALIDATION:
NOT ESTABLISHED

NEGATIVE-CASE TEST:
NOT RUN IN THIS ANALYSIS

DF-011:
NOT RUN IN THIS ANALYSIS
```

This result does not patch the method, change any gate, reconstruct evidence,
complete Part B or change an existing research status.
