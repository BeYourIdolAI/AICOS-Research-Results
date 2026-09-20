# PROSPECTIVE-DIAG-PROBE-01 — Pre-Frida mechanical fixture audit protocol

VERSION: `v0.1`

STATUS: `FROZEN BEFORE FIXTURE RECEIPT`

AUDIT TYPE: `MECHANICAL FIXTURE VERIFICATION ONLY`

DIAGNOSTICITY ASSESSMENT: `PROHIBITED IN THIS AUDIT`

FIXTURE EDITING: `PROHIBITED`

## Inputs required

- original CASE X fixture;
- original CASE Y fixture;
- original Sonnet output record or provenance sufficient to bind both files
  to that output;
- exact-byte SHA-256 for each input.

## Required checks

Each check must be answered only `YES` or `NO`, with exact source locations in
CASE X and CASE Y.

```text
1. same research question? YES required
2. same tested proposition? YES required
3. same possible outcomes? YES required
4. same named decision point? YES required
5. same execution structure? YES required
6. only varied axis = aggregation/decision semantics? YES required
```

The sixth check requires both:

- explicit aggregation/decision semantics in one case; and
- incompletely specified aggregation/decision semantics in the other case.

It does not authorize the auditor to improve, interpretively complete or
rewrite either case.

## Mechanical comparison boundary

Permitted operations:

- compare exact text and structure;
- identify named objects, inputs, outputs and decision points;
- enumerate differences;
- verify file identity and provenance;
- determine whether each required equality is textually established.

Prohibited operations:

- assess whether either case is diagnostic;
- predict the classifier's result;
- repair either fixture;
- add missing semantics;
- choose a preferred case;
- apply D1–D11 or any historical result;
- infer equivalence where the fixture text does not establish it.

## Send/no-send rule

```text
IF ALL SIX CHECKS = YES:
ELIGIBLE FOR BLIND-PACKAGE ASSEMBLY

IF ANY CHECK = NO:
DO NOT SEND TO FRIDA

IF ANY CHECK CANNOT BE MECHANICALLY DETERMINED:
YES REQUIREMENT IS NOT MET
DO NOT SEND TO FRIDA
```

This rule is a package-release condition for this probe. It is not a new
diagnosticity gate or research primitive.

## Required audit output

The future audit record must contain:

- source filename, byte count and SHA-256 for both fixtures;
- provenance of the Sonnet output;
- one `YES` or `NO` result for each required check;
- exact source evidence for each result;
- an exhaustive textual difference inventory;
- final package eligibility: `ELIGIBLE` or `DO NOT SEND`;
- confirmation that no fixture bytes were modified;
- SHA-256 for the frozen audit record.

No fixture is present or audited in this protocol document.

