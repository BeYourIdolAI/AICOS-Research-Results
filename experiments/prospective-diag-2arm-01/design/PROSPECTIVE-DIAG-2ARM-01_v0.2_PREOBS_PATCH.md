# PROSPECTIVE-DIAG-2ARM-01 — v0.2 PRE-OBSERVATION PATCH

STATUS: PATCH, FROZEN BEFORE OBSERVATION
PARENT: PROSPECTIVE-DIAG-2ARM-01 v0.1
PARENT_FREEZE_MANIFEST: FINAL_FREEZE_MANIFEST.json
PARENT_FREEZE_MANIFEST_SHA256: 7e9724e5f3201b4f1ad08ff298e3bb1d8ae3d090bbd2d867e5be6cc33454a1f5
SCOPE: Implementation-contract patch only. The v0.1 freeze is preserved unchanged as historical evidence and is not superseded, overwritten, or reinterpreted by this document.

## RELATION TO v0.1 UNRESOLVED SECTION
v0.1 stated: "If the actual target runtime cannot expose stable target/configuration identity or raw terminal bytes, that implementation deficiency must be resolved before execution; it must not be patched by post-hoc judgment." This patch resolves that class of implementation gap for request-byte identity and RAW/parser input shape, before any execution occurs.

## NOT CHANGED BY THIS PATCH
The following remain exactly as frozen in v0.1 and are not touched, reinterpreted, or superseded by this document:

- PROPOSITION (unchanged)
- CORPUS — CORPUS_MANIFEST.json (unchanged, sha256 868f961fce9ef219af1eb292d56d7afcf5bce4b6ea6ecade22f86f128a442324)
- TARGET / SYSTEM identity and execution configuration — TARGET_CONFIGURATION_MANIFEST.json (unchanged, sha256 c130a1a101b75076efebeee0b659e146f1107f7feaee52da0ba2aa9c2b8b9376)
- PROMPT TEXT — system_prompt_exact and exact_template (unchanged)
- EFFECT THRESHOLD — DELTA >= 0.20 (unchanged)
- PARSER SCORING SEMANTICS — FALSE_ADOPTION / OTHER_ERROR / INVALID rules in PARSER_SCORER.py (unchanged, sha256 f4c8c76afe1baef4d17d0aba31fb44a2d0fca02e96ae92d1bfc982435ba828f5)
- RETRY SEMANTICS (unchanged)
- CONCLUSION RULE — CONCLUSION_LOGIC.py (unchanged, sha256 9b94ebdc6b09f55ed412ed4004e502117551d0f3bf4d8655ae729bb970c052a2)

No byte of any v0.1 component is modified by this patch. This patch adds one new frozen component (this file) and a runtime bundle reassertion; it does not alter the five v0.1 components' identity.

## PATCH 1 — REQUEST BYTE DEFINITION

`request_bytes` is defined as the deterministic UTF-8 serialization of the complete logical request, containing both frozen prompt components:

```
{
  "system_prompt": "<exact frozen system prompt>",
  "user_prompt": "<exact mechanically rendered user prompt>"
}
```

Canonical serialization:

```
UTF-8
ensure_ascii=false
sort_keys=true
separators=(",",":")
trailing newline=false
```

`request_b64` and `request_sha256`, as consumed by the frozen `PARSER_SCORER.py` RAW contract, MUST refer exactly to those canonical bytes — i.e. `request_b64 = base64(canonical_bytes)` and `request_sha256 = sha256_hex(canonical_bytes)`.

The actual `llama.cpp` invocation MUST use the same two strings separately, through the frozen `--system-prompt` and `--prompt` interfaces, rather than the combined JSON object. The combined JSON object exists only to give `request_bytes` a single deterministic canonical form for hashing/provenance; it is never sent to the runtime as one payload.

`system_prompt` in the canonical object is `system_prompt_exact` from TARGET_CONFIGURATION_MANIFEST.json, byte for byte. `user_prompt` is the mechanically rendered string produced by `user_prompt_rendering.exact_template` ("records-json-then-question-v1") from TARGET_CONFIGURATION_MANIFEST.json, applied to the selected arm's `records` and `question` from CORPUS_MANIFEST.json, exactly as already specified there. This patch introduces no new rendering rule — it only fixes how the two already-frozen strings are combined and hashed for provenance.

## PATCH 2 — RAW / PARSER CONTRACT

The authoritative experiment data — `T_i`, `F_i`, input records, question, and target configuration — remain referenced from the already-frozen corpus/config artifacts (CORPUS_MANIFEST.json, TARGET_CONFIGURATION_MANIFEST.json) and are not duplicated into RAW.

Each RAW JSONL trial supplied to `PARSER_SCORER.py` contains exactly the schema already required by the frozen parser:

```
trial_id
arm
item_id
target_configuration_sha256
attempts
```

No duplicated corpus fields (`T_i`, `F_i`, records, question, or any rendering of them) are inserted into that parser input. The RAW trial records execution observations only — request/response bytes and hashes, attempt metadata, timestamps, terminal-delivery and infrastructure-error state — while the frozen corpus/config artifacts remain the sole source of normative input data, exactly as PARSER_SCORER.py's `load_corpus`/`score_trial` already assume.

This patch makes explicit and binding a constraint that was already true of the frozen parser's behavior (it looks up `item` and `T_i`/`F_i` from the corpus by `item_id`, never from the trial record); it changes no code and no parsing/scoring logic.

## WHAT THIS PATCH DOES NOT DO

- Does not execute the target.
- Does not alter the bytes of PARSER_SCORER.py or CONCLUSION_LOGIC.py; their v0.1 hashes remain normative and unchanged.
- Does not add, remove, reorder, or reweight any item in the corpus.
- Does not change the 0.20 effect threshold, the control-viability criteria, or the four allowed conclusion outcomes.
- Does not perform, simulate, or analyze any observation.
- Does not apply, reference, or expose any D1–D11 or later Diagnosticity-method material.

## FREEZE RULE

This patch must be hash-bound, together with the unchanged v0.1 five components and a runtime bundle record, into a new v0.2 freeze manifest before any runner/harness code executes the target, and before any Diagnosticity-method analysis is applied. Any later change creates a new version and a new hash; it must not overwrite this patch or the v0.1 specification.
