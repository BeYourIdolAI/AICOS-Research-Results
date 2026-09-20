# AICOS — Research, Measurement and Assurance

This repository preserves AICOS research artifacts, experimental history, and their evidentiary boundaries.

`OBSERVATION ≠ INTERPRETATION ≠ CLAIM ≠ DECISION ≠ PRODUCT VALUE`

Evidence outranks model confidence, consensus, authority, or fluency. Negative results, failed executions, superseded implementations, and unresolved findings are intentionally preserved.

The repository follows the principle:

`RAW → LOGS → RESULTS → REPORT`

Reports and later interpretations do not replace historical observations.

## Repository scope

Current material includes several distinct research records.

### EAW v0.4.8 / P4 archival packet

The repository contains the previously published partial archival research packet for EAW v0.4.8 / P4 same-Q composition.

That packet is incomplete by design and preserves its original claim boundaries. It does not represent the complete historical P4 evidence record.

See:

`eaw/v0.4.8/`

The included EAW candidate is a logical and epistemic research object, not an implemented security product.

### PROSPECTIVE-DIAG-2ARM-01

The repository preserves:

- the frozen prospective design;
- pre-observation patches;
- multiple runner/harness iterations;
- preserved failed, stalled, and invalid executions;
- `EXECUTION_005`, whose frozen result remained `INVALID_CONTROL`;
- trace-integrity and pairwise analyses.

Negative and unsuccessful runs are retained as part of the research record rather than replaced by later executions.

See:

`experiments/prospective-diag-2arm-01/`

### PROSPECTIVE-MAGNITUDE-01

This separately frozen prospective experiment tested whether assigning the numerically larger value to `SECONDARY_NOTE` changed source selection under its exact fixture.

Its completed `EXECUTION_001` reported a prospectively defined paired descriptive effect of:

`+26.67 percentage points`

under that specific frozen setup.

This result does not by itself establish a general model preference for larger values, a general causal mechanism, or an explanation of the earlier `EXECUTION_005` result.

See:

`experiments/prospective-magnitude-01/`

### Additional research context

The repository also contains non-canonical historical research context recovered from additional local sources.

These materials are retained for provenance and research-history purposes and must not be silently promoted to canonical evidence.

See:

`research-context/`

## Claim boundary

Material in this repository does not by itself establish:

- general model behavior;
- system-level enforcement;
- security validation;
- assurance validity;
- product readiness;
- external validation;
- mitigation of any external incident;
- that AICOS or EAW solves a general alignment or reliability problem.

Claims remain local to the evidence and experimental scope that supports them.

## Navigation

Start with:

- `ARTIFACT_INDEX.md` — artifact roles, status, paths, hashes, and evidentiary type;
- `RESEARCH_HISTORY.md` — chronological research history;
- `PUBLICATION_STATUS.md` — publication-preparation and privacy status;
- `inventory/` — staging, classification, provenance, and publication-review records.

Historical artifacts should be interpreted together with their manifests, hashes, provenance records, and explicit status.
