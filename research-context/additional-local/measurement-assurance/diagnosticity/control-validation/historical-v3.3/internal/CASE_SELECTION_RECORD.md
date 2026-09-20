# AICOS Diagnosticity — Historical Control Case Selection Record

STATUS: SELECTED FOR BLIND CLASSIFICATION

CASE ID: HIST-DIAG-CTRL-01

SELECTED CASE: AI Council OS v3.3 — Valideringsplan v1

## Selection rule

Select the first historical experiment before the Diagnosticity method pack that:

1. has a sufficiently complete preregistration, result and review/correction chain;
2. did not contribute to the construction of D1–D11; and
3. can be presented to the classifier without the D1–D11 method, the current
   evidence-basis diagnosis or a predicted classification.

This rule was fixed before comparing the historical candidates below.

## Selected immutable snapshot

Repository: `BeYourIdolAI/ai-council-os`

Review/correction snapshot:
`a9e27559c9548522d3def2e1843a1ccf79efa4f2`

The preregistration file has its own earlier commit:
`85e11bc89d373cd0120d89c47972f97412ecee20`

GitHub records that commit with the message:
`Valideringsplan v1 — låst före testkörning`

The final report first appeared on 2026-08-19. The selected 2026-08-21
snapshot contains the subsequently verified validation corrections. A later
2026-08-23 documentation commit by `jimbofrida` is outside the selected
snapshot.

## Eligibility assessment

PRE-DIAGNOSTICITY: YES

The v3.3 plan was committed on 2026-08-11 and the result chain was completed
and corrected by 2026-08-21. The Diagnosticity method material in the local
workspace is later.

NOT USED TO CONSTRUCT D1–D11: SUPPORTED WITHIN AVAILABLE METHOD RECORD

The uploaded original Diagnosticity prompt and method pack identify AT4-01,
AT1-01 and AT3-01 as the source experiments. They do not identify v3.3,
Valideringsplan v1 or its five scenarios as source experiments. This establishes
absence from the explicit source list; it cannot prove absence from every
person's background knowledge.

PREREGISTRATION: MECHANICALLY TIME-ORDERED IN GIT

The plan was committed as locked before test execution. The plan fixes the
model-comparison design, five scenarios, MED/UTAN conditions, repetitions,
mechanical rubric, qualitative rubric and pass conditions.

RESULT CHAIN: PRESENT WITH DISCLOSED GAPS

The repository snapshot contains the run log, scenario records, combined
result, final report and correction record. The report records 96 observations
from 100 planned runs. Runs 079, 080, 082 and 110 are missing and are not
reconstructed. The preregistered Part B blind qualitative assessment was not
performed. Part A is reported as mechanical assessment against the frozen
rubric.

REVIEW/CORRECTION CHAIN: PRESENT, NOT FULLY INDEPENDENT

Verified validation corrections were committed on 2026-08-21. The repository
does not establish a fully independent adversarial review of the whole v3.3
experiment. This limits the case but does not erase the time-ordered plan and
result record.

FRIDA EXPOSURE: MATERIAL LIMITATION

The original plan names Frida as the intended Part B assessor, although Part B
was not performed. The account `jimbofrida` later committed a documentation
correction on 2026-08-23. Therefore the proposed classifier is D1–D11-blind for
this reassessment but cannot be claimed to be case-naive. The blind packet uses
the 2026-08-21 snapshot so the later Frida-authored change is not part of the
classification evidence.

## Earlier and adjacent candidates

### v3.4 targeted regression

EXCLUDED — INSUFFICIENT ORIGINAL ARTIFACT AVAILABILITY

The v3.4 raw index states that the 40 complete anonymized answers, unblinding
key, original output and run/scoring scripts are not present in the branch.
They are source-reported as preserved elsewhere, but byte fidelity and
completeness were not audited there.

### v3.5a

EXCLUDED — BLOCKED EXECUTION

The experiment was blocked by infrastructure and does not provide a completed
result chain suitable for this control.

### v3.5b

EXCLUDED — ORIGINAL EXECUTION PACKAGE OUTSIDE REPOSITORY

The repository states that the frozen testkit, preserved completed ZIP and all
73 raw attempts remain outside the documentation-only sync.

## Parallel DF-011 locator result

ORIGINAL DF-011 CHAIN: LOCATED

Commit:
`e831a51b0fed3a6aabafa0c7d623bbce32762ffc`

Directory:
`validation/measurement-calibration/v0.2/claim_boundary_probe_v0.3/`

The directory contains a freeze manifest, protocol amendment, analysis repair,
result summary, analysis code, live-run report files and event directories
E001–E020. The historical DF-011 finding reports H1 not supported, with the
primary comparison directionally worse but inconclusive.

DF-011 is not selected as the first control because its freeze manifest and
result first appear in the same Git commit, so the repository does not
independently time-order the freeze before execution. The commit author is
also `jimbofrida`, which makes it no cleaner for a Frida-blind reassessment.

## Decision

HIST-DIAG-CTRL-01 is v3.3 Valideringsplan v1 at the immutable 2026-08-21
snapshot. Frida receives only the original case artifacts and the neutral
classification request in the sibling `blind-packet` directory.

No D1–D11 assessment has been run on this case. No predicted classification is
recorded here or in the blind packet.
