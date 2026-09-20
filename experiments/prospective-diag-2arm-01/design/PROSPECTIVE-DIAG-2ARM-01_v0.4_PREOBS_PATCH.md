# PROSPECTIVE-DIAG-2ARM-01 — v0.4 PRE-OBSERVATION PATCH

STATUS: PATCH, FROZEN BEFORE NEXT OBSERVATION
PARENT: PROSPECTIVE-DIAG-2ARM-01 v0.3
PARENT_FREEZE_MANIFEST: PROSPECTIVE-DIAG-2ARM-01_v0.3_FREEZE_MANIFEST.json
PARENT_FREEZE_MANIFEST_SHA256: 9c4cc0ca0380788206793b67bd2394a68a8898fede9128396bd5800d8da921b1
SCOPE: Implementation-contract patch only. v0.1, v0.2 and v0.3 are preserved unchanged as historical evidence and are not superseded, overwritten, or reinterpreted by this document.

## PRIOR EXECUTIONS — EVIDENCE STATUS

EXECUTION_001 through EXECUTION_004 are referenced below as motivation. **No RAW, LOGS, result, or conclusion artifact for any of EXECUTION_001–004 has been supplied to or independently verified in this review session.** Their status remains REPORTED, not ARTIFACT-BACKED. This patch does not hash-bind them and does not certify their outcome. `EXECUTION_004` remains recorded as `INVALID_CONTROL` per the requester and is explicitly not rescored by this patch (see below).

What is recorded here as REPORTED motivation only, from a local mechanical check on EXECUTION_004 stdout:
- Exact frozen `user_prompt` occurrence count in raw EXECUTION_004 stdout: 0.
- Occurrence count after a CRLF→LF transformation of that stdout: 1.
- The frozen `user_prompt` string itself contains LF line breaks and no CRLF.
- `llama-cli` stdout contains CRLF.

## NOT CHANGED BY THIS PATCH
The following remain exactly as frozen in v0.1/v0.2/v0.3 and are not touched, reinterpreted, or superseded by this document:

- PROPOSITION (unchanged)
- CORPUS — CORPUS_MANIFEST.json (unchanged, sha256 868f961fce9ef219af1eb292d56d7afcf5bce4b6ea6ecade22f86f128a442324)
- MODEL / TARGET and execution configuration — TARGET_CONFIGURATION_MANIFEST.json (unchanged, sha256 c130a1a101b75076efebeee0b659e146f1107f7feaee52da0ba2aa9c2b8b9376)
- PROMPTS (unchanged)
- EXECUTION PARAMETERS (unchanged)
- ARM ORDER (unchanged)
- EFFECT THRESHOLD — DELTA >= 0.20 (unchanged)
- PARSER SCORING SEMANTICS — PARSER_SCORER.py (unchanged, sha256 f4c8c76afe1baef4d17d0aba31fb44a2d0fca02e96ae92d1bfc982435ba828f5)
- RETRY SEMANTICS (unchanged)
- CONCLUSION LOGIC — CONCLUSION_LOGIC.py (unchanged, sha256 9b94ebdc6b09f55ed412ed4004e502117551d0f3bf4d8655ae729bb970c052a2)
- v0.2 REQUEST BYTE DEFINITION and RAW/PARSER CONTRACT (unchanged, sha256 53414251ac97a5317f2193f88b02c37ea0c8e364d8a6de4b63f4488f16197aa0)
- v0.3 RESPONSE BYTE EXTRACTION CONTRACT, steps other than the prompt-location operation (unchanged, sha256 bde31549d8ab52fca15bfde6458eb7349bd1b8696fdb8d370ebfd63ce3171d53)

This patch changes exactly one operation inside the v0.3 response-byte-extraction contract: how the frozen `user_prompt` is located inside raw stdout, so that a CRLF-vs-LF line-ending mismatch does not by itself cause a spurious extraction failure.

## DESIGN CORRECTION FROM THE REQUESTED FORM

The requested patch defined a separately materialized `stdout_match_view` (raw stdout with every CRLF replaced by LF) and located `user_prompt` inside that copy. That is not adopted as specified, because it is not boundary-safe: CRLF→LF removes one byte per replaced CRLF, so a match end-position found inside `stdout_match_view` does not correspond to the same character/byte position inside `raw_stdout_text`/`raw_stdout_bytes`. Reusing that position to slice `raw_stdout_bytes` (v0.3 step 3) would silently shift the candidate-text start boundary by the number of `\r` characters removed at or before the match — corrupting `assistant_response_bytes` for every trial with a CRLF preceding the prompt echo, without producing any error.

This patch instead matches directly against the untouched raw text, using a pattern that treats each frozen LF as equivalent to LF-or-CRLF, so no separate string is ever materialized and no position ever needs translating between two representations. This preserves the requester's stated intent (a CRLF/LF difference alone must not block the match) without introducing an index-mapping step as a new failure mode.

## PATCH — PROMPT-LOCATION MATCHING RULE (replaces v0.3 step 2 only)

1. Decode `raw_stdout_bytes` as strict UTF-8 to obtain `raw_stdout_text`. Failure => extraction failure. (v0.3 step 1, unchanged.)
2. Build `user_prompt_pattern` from the exact frozen rendered `user_prompt` string by treating every literal character as itself, except: every LF (`\n`) in `user_prompt` matches either LF (`\n`) or CRLF (`\r\n`) at that position in `raw_stdout_text`. No other character class, wildcard, or case-insensitivity is introduced.
3. Locate `user_prompt_pattern` directly in `raw_stdout_text`. It MUST match exactly once; otherwise extraction failure.
4. Begin candidate text immediately after the end of that exact match, measured in `raw_stdout_text`'s own original positions.
5. All subsequent v0.3 steps continue unchanged, renumbered: locate the first subsequent line whose first characters are exactly `[ Prompt:`; end candidate immediately before that line; remove leading and trailing CR/LF only; encode as UTF-8 without further normalization; those bytes are `assistant_response_bytes`.

`raw_stdout_bytes` is preserved exactly and is never itself CRLF-transformed. No transformation is applied to `assistant_response_bytes` beyond what v0.3 already specified. `response_b64`/`response_sha256` still refer only to `assistant_response_bytes`, never to the full transcript. `raw_stdout_b64`/`raw_stdout_sha256` in LOGS still refer to the untouched original bytes.

If `user_prompt_pattern` does not match exactly once, or if any other v0.3 extraction condition fails, the trial is not repaired by judgment; extraction failure is recorded as such under the frozen parser's existing `NO_TERMINAL_RESPONSE` / `PARSER_INVALID` handling.

## EXECUTION_004 DISPOSITION

`EXECUTION_004` remains `INVALID_CONTROL` as recorded (REPORTED) and is not rescored, reinterpreted, or retried under this patch. This patch governs only the next execution attempt.

## WHAT THIS PATCH DOES NOT DO

- Does not execute the target.
- Does not alter the bytes of PARSER_SCORER.py or CONCLUSION_LOGIC.py.
- Does not alter the v0.2 request-byte-definition or RAW/parser contract.
- Does not alter v0.3 steps other than prompt-location matching.
- Does not add, remove, reorder, or reweight any corpus item.
- Does not change the 0.20 threshold, control-viability criteria, arm order, or the four allowed conclusion outcomes.
- Does not rescore or reinterpret EXECUTION_001–004.
- Does not apply, reference, or expose any D1–D11 or later Diagnosticity-method material.

## FREEZE RULE

This patch must be hash-bound, together with the unchanged v0.1, v0.2 and v0.3 components, into a new v0.4 freeze manifest before any next execution attempt, and before any Diagnosticity-method analysis is applied. `observation_performed=false` and `experiment_execution=false` in that manifest refer specifically to the next execution under this v0.4 contract; they do not retroactively characterize EXECUTION_001–004. Any later change creates a new version and a new hash; it must not overwrite this patch or any prior frozen document.
