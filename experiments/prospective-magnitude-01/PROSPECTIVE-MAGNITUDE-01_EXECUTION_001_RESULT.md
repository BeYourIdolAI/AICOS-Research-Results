# PROSPECTIVE-MAGNITUDE-01 — EXECUTION_001 RESULT

## Status

- FREEZE COMPLETE
- EXECUTION COMPLETE
- FROZEN ANALYSIS COMPLETE
- RESULT REPORTED
- STOP

This document is a result note and handoff for the closed execution. It does not modify or replace any source artifact.

## Frozen identities

- Experiment: `PROSPECTIVE-MAGNITUDE-01`
- Execution: `EXECUTION_001`
- Planned pairs: 60
- Frozen design: `PROSPECTIVE-MAGNITUDE-01_v0.1_FROZEN.md`
- Frozen implementation contract: `PROSPECTIVE-MAGNITUDE-01_v0.2_PREOBS_IMPLEMENTATION_PATCH.md`
- Runner: `RUN_PROSPECTIVE_MAGNITUDE_01_v1.py`

The v0.1 and v0.2 freeze identities, runner identity, preexecution identity, and execution-output identities were verified against the local artifact bytes before this note was written.

## Execution result

- Complete pairs: 60
- Incomplete pairs: 0
- `OTHER_VALUE`: 0 trials
- `INVALID_FORMAT`: 0 trials
- `NO_TERMINAL_RESPONSE`: 0 trials

The runner ultimately completed normally and printed:

> RUN COMPLETE. Frozen scoring and paired analysis complete.

The temporary period with no terminal output was not established as a failure. No runner-hang defect is recorded.

## Primary descriptive result

The prospectively defined primary descriptive effect was:

`0.26666666666666666`

Equivalent descriptive statement: **+26.67 percentage points**.

Mechanical derivation:

```text
(AUTH→NOTE - NOTE→AUTH) / complete pairs
=(16 - 0) / 60
=0.26666666666666666
```

## Pairwise structure

| Pair class | Count |
|---|---:|
| AUTH→NOTE | 16 |
| NOTE→AUTH | 0 |
| AUTH→AUTH | 0 |
| NOTE→NOTE | 44 |

## Secondary basis_id observations

| Secondary attribution class | Count |
|---|---:|
| NOTE_ATTRIBUTION | 106 |
| AUTH_ATTRIBUTION | 14 |

Two `SOURCE-ATTRIBUTION ANOMALY` records were reported:

- `PAIR-030-SMALLER_NOTE`: `primary_class=AUTH_SELECTION`; `basis_class=NOTE_ATTRIBUTION`.
- `PAIR-051-SMALLER_NOTE`: `primary_class=AUTH_SELECTION`; `basis_class=NOTE_ATTRIBUTION`.

These anomalies do not establish which source the model internally relied on.

## Established observation

Under the frozen PROSPECTIVE-MAGNITUDE-01 fixture, SECONDARY_NOTE was selected more often when it carried the numerically larger value.

The prospectively defined paired net descriptive effect was **+26.67 percentage points**.

This is an observation from this exact experiment.

## Not established

This experiment does not establish:

- a general model preference for larger numbers;
- a general causal mechanism;
- why EXECUTION_005 produced its observed pattern;
- an effect of `verification_status`;
- an interaction between `verification_status` and magnitude;
- which source the model internally relied on;
- that `AUTHORITATIVE_RECORD` should normatively prevail;
- generalization to other models;
- generalization to other prompts;
- generalization to other numeric ranges;
- product or assurance validity.

## Relation to EXECUTION_005

The evidence chain is preserved as:

```text
EXECUTION_005
→ post-hoc magnitude pattern observed
→ candidate hypothesis formed
→ PROSPECTIVE-MAGNITUDE-01 designed and frozen separately
→ EXECUTION_001 produced a prospective descriptive result
```

The two experiments remain separate evidentiary objects. `EXECUTION_005` remains `INVALID_CONTROL` and is neither rewritten nor rescored by this result note.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| `PROSPECTIVE-MAGNITUDE-01_v0.1_FROZEN.md` | `9bab675eb157a51091c3c20a11304d62150e01b42c74850c46e3f8f14912c48f` |
| `MAGNITUDE_FINAL_FREEZE_MANIFEST.json` | `d25558549c4644043003963c44acd06813a6d3a117c7259c961f2d96cf354215` |
| `PROSPECTIVE-MAGNITUDE-01_v0.2_PREOBS_IMPLEMENTATION_PATCH.md` | `3bb2d08ce9d50b58704f2b9e3c73e7424c670e4a17f9730fe97da5b6fbe20789` |
| `PROSPECTIVE-MAGNITUDE-01_v0.2_FREEZE_MANIFEST.json` | `6e85cc2f8fec800bc970e2a54191660789f4fea633a12d3a253c5bca3f7df236` |
| `RUN_PROSPECTIVE_MAGNITUDE_01_v1.py` | `caababd9a7580e42fc6f2bc9f39bc0de6438db6a96b1ebd4d60117e8f689c0a0` |
| `MAGNITUDE_RUNNER_PREEXEC_RECORD_v1.json` | `81a615917c90f34a5a740317e3b803825b6682802b0493d5131ebe101363c8c4` |
| `MAGNITUDE_EXECUTION_001/RAW.jsonl` | `1e4f6168e8ee4bc4f6bfa96d12d5abc85c56ab54406fd72bdb20242cf333af29` |
| `MAGNITUDE_EXECUTION_001/LOGS.jsonl` | `de198b1e2cc207325a89154533d1d03d6bc209a23787694df85f78fa8dabdd5c` |
| `MAGNITUDE_EXECUTION_001/SCORES.jsonl` | `775f859cc847e1b25eee7a22507021f5e62408e633721f34d6dcf1ae6335586b` |
| `MAGNITUDE_EXECUTION_001/ANALYSIS.json` | `bb1568a4cba34b1a72a52d7fb1a7d982336e9f27ffb60aeac17ca617a7a9da6e` |
| `MAGNITUDE_EXECUTION_001/EXECUTION_RECORD.json` | `7ce6e3d87838d73dbac5b9c32cbfdaeba7244ba8cbe9114eefe76bd4ec3e7e73` |

## Stop condition

STOP CONDITION

This execution is closed.

No additional post-hoc analysis of the same 120 trials is part of this result note.

Any further research question must be instantiated as a separate prospective object.
