# AICOS HIST-DIAG-CTRL-01 — Retrospective D1–D11 assessment v0.1

DATE: 2026-09-20

STATUS: RETROSPECTIVE CANDIDATE-METHOD APPLICATION

NORMATIVE STATUS: NON-NORMATIVE

RESEARCH-STATUS EFFECT: NONE

## 1. Objects assessed

Historical source snapshot:
`BeYourIdolAI/ai-council-os` commit
`a9e27559c9548522d3def2e1843a1ccf79efa4f2`

Offline source package SHA-256:
`13983689d7fe819eeb7b6b446466112603981ac8dddf43e640d9e5cc04f0a10a`

Blind classification result:
`FRIDA_BLIND_CLASSIFICATION_RESULT.md`

Blind classification result SHA-256:
`ba1dae06e1ee85ec5a8d5038d8e2eabdf7ed83ec16f8ffbdf8bb59615bdf09e2`

Method object:
`AICOS_DIAGNOSTICITY_PREFLIGHT_v0.1.md`

Method SHA-256:
`3d925e198bba7aa712ffa4855d29f69d2d255334c1b1883255390882691b34ee`

Evidence-basis refinement:
`AICOS_DIAGNOSTICITY_METHOD_PACK_v0.1_EVIDENCE_BASIS_ADDENDUM_01.md`

Addendum SHA-256:
`dd1f124bfa0e812a2a0019450b595445e13ab69d18b750397c4e98d6ad5c1301`

## 2. Ordering and independence boundary

Frida's classification was completed before this assessment and without the
D1–D11 materials in her packet.

Her preserved result is:

```text
CLASSIFICATION:
DIAGNOSTIC

CONFIDENCE:
MEDIUM-HIGH
```

That result is not rewritten, re-scored or promoted here.

D1–D11 did not exist as the experiment's pre-execution checklist. This is a
retrospective method application and cannot establish that the historical team
passed the later preflight before execution.

## 3. Claim and comparison unit used here

The narrow test object is the package-level comparison:

```text
MED:
same model + scenario prompt + applicable role file + Council Operating Protocol

UTAN:
same model + same scenario prompt + no system prompt
```

The assessment concerns whether this package-level comparison was diagnostic
for the predefined Del A behaviors in the five tested scenarios. It does not
attempt to attribute an effect to any single rule or document.

## 4. Gate assessment

### D1 — SAME TARGET

RESULT: SATISFIED WITHIN THE PACKAGE-LEVEL COMPARISON

The frozen plan assigns the same scenario prompt, model family and tested
behavior to MED and UTAN. The intended difference is the Council package.
The proposition and outcome category do not change between the two arms of a
scenario.

LIMITATION:
The repository does not contain a separate raw file for every recorded
observation, so exact prompt equality cannot be rechecked independently for all
96 completed observations.

### D2 — SINGLE AXIS

RESULT: SATISFIED FOR PACKAGE EFFECT; NOT FOR COMPONENT ATTRIBUTION

At the declared experimental level, the varied factor is presence or absence
of the Council package. The package contains both a role file and the Council
Operating Protocol. The experiment therefore cannot isolate either component.

The original manual/API difference in S4 MED is a second execution axis for
runs 001–010. The plan record reports an API rerun as 041–050 with the same
10/10 refusal outcome. The manual runs must not be used as the sole basis for
the S4 comparison.

### D3 — EXPLICIT DEPENDENCY

RESULT: SATISFIED FOR THE FROZEN DESIGN; RESULT TRACE INCOMPLETE

The packaged role files and protocol contain direct rules corresponding to the
predefined scenario behaviors: source discipline, legal-outcome restraint,
critical review, role routing and open calculation. These are frozen TEXT
dependencies rather than later fixture inventions.

The design dependency is established. Complete observation-level verification
is not established because several referenced output files are absent from the
snapshot.

### D4 — CONTROL VIABILITY

RESULT: SATISFIED UNDER A COMPARATIVE-BASELINE READING

UTAN is a functioning untreated comparator: it produced usable responses in
all scenario families and matched MED on the observed S5 calculation outcome.
There is no evidence that the comparator was generally unable to answer.

METHOD-SCOPE LIMITATION:
D4 is written for an H_FULL/control conformance structure. This historical
study uses an untreated behavioral baseline. Literal H_FULL conformance is not
defined for UTAN, so this result depends on the comparative-baseline reading
rather than the method's original attack-fixture form.

### D5 — ATTACK-SENSITIVE BLOCKER

RESULT: UNRESOLVED / NOT MAPPED

The historical plan does not define one blocker B with the required matrix:

```text
B(H_CONTROL) = FALSE
B(H_ATTACK) = TRUE
```

It defines several behavioral outcomes across five scenarios. Some favor MED,
one is neutral, and one is negative for MED. No evidence-bounded mapping turns
those outcomes into one attack-sensitive blocker without adding a new judgment.

The evidence-basis addendum already records D5 source mapping as unresolved.
No intuitive mapping is introduced here.

METHOD STOP CONDITION: TRIGGERED FOR A SINGLE GLOBAL D1–D11 VERDICT

### D6 — NON-TAUTOLOGICAL DISCRIMINATION

RESULT: SATISFIED

Presence of the Council package is not identical to any scored outcome. The
model could follow, ignore or be harmed by the package. The observed mixture of
positive, neutral and negative scenario results demonstrates that the outcome
was not fixed merely by assigning MED or UTAN.

### D7 — NO CONCLUSION STIPULATION

RESULT: SATISFIED

The plan stipulates prompts, treatment objects and scoring criteria. It does
not stipulate which arm succeeds. S1 in particular returned a result contrary
to a general positive expectation.

### D8 — TYPE PRESERVATION

RESULT: PARTIALLY SATISFIED

The snapshot distinguishes plan, logs, preserved responses, results, report
and correction record. Missing observations remain marked missing, and the
summaries do not claim to be reconstructed raw output.

However, the complete set of observation-level raw outputs is not present.
Logs and aggregate summaries therefore cannot be treated as byte-level raw
evidence for every reported observation. This assessment does not make that
substitution.

### D9 — SEMANTIC COMPLETENESS

RESULT: AMBIGUOUS FOR COMPLETE INDEPENDENT VERIFICATION

Many outcome predicates are operationally clear within a scenario, including
whether a LinkedIn post was written, whether all three supplied unsupported
figures were flagged, and whether the arithmetic was correct.

The following load-bearing points remain incomplete or ambiguous:

- the full raw output set is absent;
- runs 079, 080, 082 and 110 are missing;
- the record does not contain a separate completed mechanical scoring sheet
  for every observation;
- `mätbart bättre` is not assigned a numerical difference threshold in the
  frozen plan;
- some fabrication/source judgments cannot be independently replayed from a
  corresponding raw file in the snapshot.

These gaps prevent a determinate all-trace PASS under D9. They do not erase the
clearer preserved scenario contrasts.

METHOD STOP CONDITION: TRIGGERED FOR COMPLETE TRACE CERTIFICATION

### D10 — OUTCOME-LAYER SEPARATION

RESULT: SATISFIED WITHIN FRIDA'S CLAIM BOUNDARY

Frida's result concerns observed runtime behavior in the tested scenarios. It
does not convert those observations into general enforcement, general model
safety, component-level causation or cross-model validity. Del B is explicitly
kept separate and unperformed.

Stronger historical report language must not enlarge this narrower result.

### D11 — FALSIFIABILITY CHECK

RESULT: SATISFIED

Before execution, the plan describes multiple fixture-consistent results for
each scenario: desired behavior, failure, equality and loss of usefulness. The
observed record contains positive, neutral and negative results. A different
conclusion was therefore possible within the frozen design.

## 5. Gate summary

| Gate | Result |
|---|---|
| D1 | SATISFIED WITHIN PACKAGE-LEVEL COMPARISON |
| D2 | SATISFIED FOR PACKAGE EFFECT; NOT COMPONENT ATTRIBUTION |
| D3 | DESIGN DEPENDENCY SATISFIED; RESULT TRACE INCOMPLETE |
| D4 | SATISFIED UNDER COMPARATIVE-BASELINE READING |
| D5 | UNRESOLVED / NOT MAPPED |
| D6 | SATISFIED |
| D7 | SATISFIED |
| D8 | PARTIALLY SATISFIED |
| D9 | AMBIGUOUS FOR COMPLETE INDEPENDENT VERIFICATION |
| D10 | SATISFIED WITHIN THE NARROW CLAIM BOUNDARY |
| D11 | SATISFIED |

## 6. D1–D11 result

```text
GLOBAL METHOD RESULT:
AMBIGUOUS

DETERMINATE ALL-GATE PASS:
NOT ESTABLISHED

PRIMARY REASONS:
D5 UNRESOLVED / NOT MAPPED
D9 INCOMPLETE FOR FULL TRACE CERTIFICATION
```

This is not a reclassification of Frida's result. The two outputs answer
different questions:

```text
FRIDA'S PRECOMMITTED COMPARATIVE CRITERIA:
DIAGNOSTIC WITHIN DEL A / TESTED-SCENARIO SCOPE

RETROSPECTIVE FULL D1–D11 CERTIFICATION:
AMBIGUOUS
```

## 7. Method observation

The case supplies evidence that D1, D2, D6, D7 and D11 can recognize important
features of a falsifiable comparative experiment. It also exposes a scope
question: D5 is formulated for attack-sensitive blocker experiments and does
not directly map to a multi-outcome intervention study.

This is a candidate method-scope observation. It does not establish that D5 is
wrong, that D1–D11 are invalid, or that the method should be patched. A method
change requires separate review.

## 8. Preserved limitations

- 96 of 100 planned runs have recorded data.
- Runs 079, 080, 082 and 110 remain missing.
- Missing runs are not reconstructed.
- The full observation-level raw file set is not present.
- Part B was not performed.
- No Part B claim is inferred.
- The package effect is not decomposed into individual component effects.
- No general AICOS effectiveness, hallucination prevention or cross-model
  generalization claim is established.
- No research status is changed by this assessment.
