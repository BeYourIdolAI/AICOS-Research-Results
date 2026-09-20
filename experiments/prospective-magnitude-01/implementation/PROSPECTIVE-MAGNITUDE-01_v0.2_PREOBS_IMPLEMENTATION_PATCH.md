# PROSPECTIVE-MAGNITUDE-01 v0.2 — PRE-OBSERVATION IMPLEMENTATION PATCH

## Status and scope

This patch defines only artifact schemas and mechanical adapters between the already frozen v0.1 components. It changes no proposition, corpus value, prompt, verification status, execution order, outcome semantic, complete-pair definition, descriptive-effect formula, retry rule, target configuration, frozen scorer, or frozen analysis. No target observation or experiment execution occurred.

## RAW contract

`MAGNITUDE_EXECUTION_001/RAW.jsonl` contains exactly 120 JSONL objects, one per planned trial, with exactly these top-level fields: `trial_id`, `pair_id`, `condition`, `target_configuration_sha256`, `attempts`. `condition` is `SMALLER_NOTE` or `LARGER_NOTE`.

Each attempt has exactly: `attempt_id`, `request_b64`, `request_sha256`, `response_b64`, `response_sha256`, `terminal_delivered`, `infrastructure_error`, `start_timestamp`, `end_timestamp`. Response bytes and hash refer exactly to extracted assistant-response bytes under the frozen extraction contract. They are null together for a nonterminal attempt. Full stdout is not duplicated in RAW.

One or two attempts are permitted. A second attempt is valid only when the first is nonterminal and has a non-null infrastructure error. Retry request bytes and hashes must be identical. At most one attempt may be terminal. The adapter selects the sole terminal attempt, or the final attempt when none is terminal.

## LOGS contract

`MAGNITUDE_EXECUTION_001/LOGS.jsonl` contains an attempt record with at least: `trial_id`, `pair_id`, `condition`, `attempt_id`, `request_sha256`, `response_sha256`, `raw_stdout_b64`, `raw_stdout_sha256`, `extraction_error`, `stderr_b64`, `stderr_sha256`, `process_returncode`, `terminal_delivered`, `infrastructure_error`, `start_timestamp`, `end_timestamp`. Extra mechanical runtime fields are permitted and do not affect scoring. `raw_stdout_b64` preserves the complete untouched stdout bytes.

## Score adapter and SCORES contract

`MAGNITUDE_SCORE_ADAPTER.py` verifies trial identity against the frozen plan, validates request/response hashes and retry shape, retrieves the frozen corpus condition, and calls the unchanged frozen API exactly as:

```python
MAGNITUDE_PARSER_SCORER.score_trial(
    selected_attempt["response_b64"],
    frozen_condition,
    selected_attempt["terminal_delivered"],
)
```

It writes exactly 120 records to `MAGNITUDE_EXECUTION_001/SCORES.jsonl`. Required adapter fields are `trial_id`, `pair_id`, `condition`, `primary_class`, `returned_value`, `basis_id`, `basis_class`, `source_attribution_consistent`, `source_raw_response_sha256`, plus `frozen_scorer_output`, which preserves the complete unchanged scorer return object.

Exact scorer-to-SCORES mapping:

| Frozen scorer output | SCORES field | Mapping |
|---|---|---|
| `primary_outcome` | `primary_class` | Identity |
| `returned_value` | `returned_value` | Identity; absent becomes null |
| `basis_id` | `basis_id` | Identity; absent becomes null |
| `attribution` | `basis_class` | Identity; absent becomes null |
| `source_attribution_anomaly` | `source_attribution_consistent` | Logical negation only for AUTH_SELECTION or NOTE_SELECTION; otherwise null |
| complete scorer dict | `frozen_scorer_output` | Preserved unchanged |
| selected terminal attempt `response_sha256` | `source_raw_response_sha256` | Identity; null when no terminal response |

No parsing or scoring semantic is duplicated in the adapter.

## Pair-analysis adapter and ANALYSIS contract

`MAGNITUDE_PAIR_ANALYSIS_ADAPTER.py` verifies 120 scores against the frozen plan, requires exactly one condition of each kind for every one of 60 pair IDs, and constructs for each pair:

```python
{
  "pair_id": pair_id,
  "SMALLER_NOTE": {"primary_outcome": smaller_score["primary_class"]},
  "LARGER_NOTE": {"primary_outcome": larger_score["primary_class"]}
}
```

It passes the 60 objects directly to the unchanged frozen `MAGNITUDE_ANALYSIS.analyze_pairs()`.

`MAGNITUDE_EXECUTION_001/ANALYSIS.json` contains the required hashes, pair counts, mapped pair-class counts, primary descriptive effect, mechanical trial counts, secondary basis summary, incomplete pairs, and `frozen_analysis_output` preserving the complete unchanged analysis return object.

Exact frozen-analysis-to-ANALYSIS mapping:

| Frozen `analyze_pairs()` output | ANALYSIS field | Mapping |
|---|---|---|
| `complete_pair_count` | `complete_pair_count` | Identity |
| `incomplete_pair_count` | `incomplete_pair_count` | Identity |
| `pair_class_counts["AUTH→NOTE"]` | `pair_class_counts.AUTH_TO_NOTE` | Identity |
| `pair_class_counts["NOTE→AUTH"]` | `pair_class_counts.NOTE_TO_AUTH` | Identity |
| `pair_class_counts["AUTH→AUTH"]` | `pair_class_counts.AUTH_TO_AUTH` | Identity |
| `pair_class_counts["NOTE→NOTE"]` | `pair_class_counts.NOTE_TO_NOTE` | Identity |
| `PRIMARY_DESCRIPTIVE_EFFECT` | `primary_descriptive_effect` | Numeric identity; `NOT_COMPUTABLE` maps to null |
| `PRIMARY_DESCRIPTIVE_EFFECT` | `primary_descriptive_effect_frozen_value` | Preserved unchanged, including `NOT_COMPUTABLE` |
| `incomplete_pairs` | `incomplete_pairs` | Identity |
| complete analysis dict | `frozen_analysis_output` | Preserved unchanged |

`other_value_trial_count`, `invalid_format_trial_count`, and `no_terminal_response_trial_count` are direct counts of corresponding `primary_class` values in SCORES. `basis_secondary_summary` is a direct count of `basis_class` plus records whose `source_attribution_consistent` is false. These mechanical summaries do not affect the frozen pair analysis.

No SUPPORTS, CONTRADICTS, PASS, FAIL, threshold, or conclusion layer is added. ANALYSIS.json is the final analytical artifact.

## Execution record binding

At execution, `MAGNITUDE_EXECUTION_001/EXECUTION_RECORD.json` must hash-bind: runner, preexec record, final v0.2 freeze manifest, original v0.1 freeze manifest, corpus, plan, target configuration, frozen scorer, frozen analysis, score adapter, pair-analysis adapter, model, and llama-cli, plus execution start timestamp.

## Synthetic adapter verification

Before this patch was frozen, syntax and non-target adapter tests passed for NOTE_SELECTION, AUTH_SELECTION, OTHER_VALUE, INVALID_FORMAT, NO_TERMINAL_RESPONSE, all four complete pair classes, incomplete pairs, zero complete pairs, value/basis mismatch, a 120-record RAW adapter integration, and a 120-score pair adapter integration. Adapter output was compared to the unchanged frozen scorer/analysis output. No target was called.

## Freeze boundary

`observation_performed=false` and `experiment_execution=false`. No `MAGNITUDE_EXECUTION_001` directory was created. Any change to a bound v0.1 or v0.2 component requires a new prospective freeze before observation.
