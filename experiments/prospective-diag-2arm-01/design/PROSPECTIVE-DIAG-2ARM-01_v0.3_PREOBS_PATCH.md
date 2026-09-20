# PROSPECTIVE-DIAG-2ARM-01 — v0.3 PRE-OBSERVATION PATCH

STATUS: PATCH, FROZEN BEFORE NEXT OBSERVATION
PARENT: PROSPECTIVE-DIAG-2ARM-01 v0.2
PARENT_FREEZE_MANIFEST: PROSPECTIVE-DIAG-2ARM-01_v0.2_FREEZE_MANIFEST.json
PARENT_FREEZE_MANIFEST_SHA256: e62a2d6cc7901c0592b1ef3e659ae2cf4b33f74c637c186cb55ca663b05b3394
SCOPE: Implementation-contract patch only. v0.1 and v0.2 are preserved unchanged as historical evidence and are not superseded, overwritten, or reinterpreted by this document.

## PRIOR EXECUTIONS — EVIDENCE STATUS

EXECUTION_001, EXECUTION_002 and EXECUTION_003 are referenced below as the motivation for this patch, as reported. **No RAW, LOGS, result, or conclusion artifact for EXECUTION_001, EXECUTION_002, or EXECUTION_003 has been supplied to or independently verified in this review session.** Their status here is REPORTED, not ARTIFACT-BACKED. This patch does not hash-bind them, does not assert their byte identity, and does not certify their outcome. If they are to be hash-bound as historical evidence, their actual RAW/result artifacts must be supplied and hashed directly — not reconstructed from description.

What is recorded here as REPORTED motivation only:
- EXECUTION_003 reportedly completed 120/120 trials but scored `PARSER_INVALID` on all 120, attributed to `llama-cli.exe` stdout containing runtime banner, echoed prompt, generated assistant text, performance footer, and exit text — none of which the frozen `PARSER_SCORER.py` response contract expects.
- A separate non-corpus smoke test reportedly confirmed `--log-disable` and `--no-perf` do not remove this transcript framing.

This patch treats that as the reason a response-byte-extraction contract is needed upstream of the frozen parser. It does not treat it as a confirmed, artifact-verified finding.

## NOT CHANGED BY THIS PATCH
The following remain exactly as frozen in v0.1/v0.2 and are not touched, reinterpreted, or superseded by this document:

- PROPOSITION (unchanged)
- CORPUS — CORPUS_MANIFEST.json (unchanged, sha256 868f961fce9ef219af1eb292d56d7afcf5bce4b6ea6ecade22f86f128a442324)
- TARGET / SYSTEM identity and execution configuration — TARGET_CONFIGURATION_MANIFEST.json (unchanged, sha256 c130a1a101b75076efebeee0b659e146f1107f7feaee52da0ba2aa9c2b8b9376)
- PROMPTS — system_prompt_exact and exact_template (unchanged)
- EXECUTION PARAMETERS (unchanged)
- ARM ORDER (unchanged)
- EFFECT THRESHOLD — DELTA >= 0.20 (unchanged)
- PARSER SCORING SEMANTICS — FALSE_ADOPTION / OTHER_ERROR / INVALID rules in PARSER_SCORER.py (unchanged, sha256 f4c8c76afe1baef4d17d0aba31fb44a2d0fca02e96ae92d1bfc982435ba828f5)
- RETRY SEMANTICS (unchanged)
- CONCLUSION RULE — CONCLUSION_LOGIC.py (unchanged, sha256 9b94ebdc6b09f55ed412ed4004e502117551d0f3bf4d8655ae729bb970c052a2)
- v0.2 REQUEST BYTE DEFINITION and RAW/PARSER CONTRACT (unchanged, sha256 53414251ac97a5317f2193f88b02c37ea0c8e364d8a6de4b63f4488f16197aa0)

This patch adds exactly one new contract, applied upstream of the frozen parser: how `assistant_response_bytes` is extracted from raw `llama-cli` stdout before `response_b64`/`response_sha256` are computed.

## PATCH — RESPONSE BYTE EXTRACTION CONTRACT

Define:

```
raw_stdout_bytes = exact bytes captured from llama-cli stdout.
```

Define `assistant_response_bytes` deterministically:

1. Decode `raw_stdout_bytes` as strict UTF-8. Failure => extraction failure.
2. Locate the exact frozen rendered `user_prompt` string. It MUST occur exactly once; otherwise extraction failure.
3. Begin candidate text immediately after the exact `user_prompt`.
4. Locate the first subsequent line whose first characters are exactly `[ Prompt:`.
5. End candidate immediately before that line.
6. Remove leading and trailing CR (`\r`) and LF (`\n`) characters only.
7. Encode the remaining candidate as UTF-8 without further normalization.
8. Those exact bytes are `assistant_response_bytes`.

`response_b64` and `response_sha256`, as consumed by the frozen `PARSER_SCORER.py`, MUST refer to `assistant_response_bytes` — never to the complete unmodified runtime stdout transcript.

The full unmodified runtime stdout MUST also be preserved separately in LOGS as:

```
raw_stdout_b64
raw_stdout_sha256
```

No semantic parsing, JSON repair, markdown removal, whitespace normalization beyond boundary CR/LF removal, or selection among multiple candidate answers is permitted. If any extraction condition fails (non-UTF-8, `user_prompt` not found exactly once, `[ Prompt:` marker not found), the trial is not repaired by judgment — extraction failure is recorded as such and the trial remains INVALID under the frozen parser's existing `NO_TERMINAL_RESPONSE` / `PARSER_INVALID` handling; no new conclusion category is introduced.

## WHAT THIS PATCH DOES NOT DO

- Does not execute the target.
- Does not alter the bytes of PARSER_SCORER.py or CONCLUSION_LOGIC.py; their hashes remain normative and unchanged.
- Does not alter the v0.2 request-byte-definition or RAW/parser contract.
- Does not add, remove, reorder, or reweight any item in the corpus.
- Does not change the 0.20 effect threshold, control-viability criteria, arm order, or the four allowed conclusion outcomes.
- Does not certify, score, or draw a conclusion from EXECUTION_001, EXECUTION_002, or EXECUTION_003.
- Does not apply, reference, or expose any D1–D11 or later Diagnosticity-method material.

## FREEZE RULE

This patch must be hash-bound, together with the unchanged v0.1 and v0.2 components, into a new v0.3 freeze manifest before any next execution attempt under this contract, and before any Diagnosticity-method analysis is applied. `observation_performed=false` and `experiment_execution=false` in that manifest refer specifically to the next execution under this v0.3 contract; they do not retroactively assert anything about EXECUTION_001–003, which are recorded separately as REPORTED prior events, not as artifacts this freeze verifies. Any later change creates a new version and a new hash; it must not overwrite this patch or any prior frozen document.
