## CASE Y

**WHAT IS BEING TESTED**
Whether Model M's outputs on Task Set T meet a stated quality threshold, as judged by Evaluator Panel E, relative to a baseline condition.

**WHAT CAN BE OBSERVED**
240 raw evaluator verdicts (PASS / FAIL / INVALID) across 2 conditions × 40 tasks × 3 evaluator passes per output.

**WHAT DECISION THE EXPERIMENT IS INTENDED TO INFORM**
Whether the proposition "Model M meets quality threshold θ = 0.75 and exceeds the Condition B baseline" is SUPPORTED or NOT SUPPORTED, decided once all 240 verdicts are collected.

**Research question:** Does Model M's aggregate output quality on Task Set T reach θ = 0.75 and exceed the Condition B baseline, as judged by Evaluator Panel E?

**Proposition/hypothesis:** H: Model M's aggregate quality on Task Set T is ≥ θ = 0.75 and exceeds Condition B's aggregate quality.

**Two comparable conditions:**
- Condition A: Model M, checkpoint v2.3, temperature 0, single-pass generation
- Condition B: Model M-baseline, prior fixed checkpoint, temperature 0, single-pass generation

**Model:** Generation — Model M v2.3 (fixed checkpoint hash recorded). Evaluation — Evaluator E, fixed checkpoint, temperature 0.

**Prompts:** Generation template G1 (task instructions + input, no chain-of-thought scaffold). Evaluator template J1 (rubric text + task input + model output → binary PASS/FAIL verdict, no aggregation instructions embedded in the item-level prompt).

**Execution conditions:** 40 tasks × 2 conditions, each run once at temperature 0. Each output scored independently by 3 evaluator passes (E1–E3), each a fresh context, temperature 0.

**Number of runs:** 40 × 2 × 3 = 240 evaluator judgments; 80 generation calls.

**Possible observable outcomes:** Item-pass level — PASS / FAIL / INVALID. Conclusion level — SUPPORTED / NOT SUPPORTED.

**Measurement variables:** task_id, condition, evaluator_pass_id, verdict, timestamp; condition-level aggregate score; final conclusion label.

**Decision point named before running:** After all 240 verdicts are collected, it will be decided whether the proposition (θ = 0.75, exceeding Condition B) is SUPPORTED or NOT SUPPORTED.

**Raw data format:** JSONL, one line per (task_id, condition, evaluator_pass_id): {generation_output_text, evaluator_id, evaluator_pass_id, verdict_raw_text, timestamp}.

**Log format:** Append-only run log, one line per API call: {call_id, model, prompt_template_id, input_hash, output_hash, timestamp, latency_ms, token_counts}.

**Scoring inputs:** The 240 raw verdict strings + task_id + condition. Nothing else (no evaluator rationale text, no confidence scores, no cross-item information).

**Other provenance:** Fixed seeds for any sampling step; fixed model/evaluator checkpoint hashes; prompt template version IDs; harness git commit hash recorded per run.

**Aggregation / decision semantics — left incomplete before observation:**
The exact aggregation rule (e.g., majority vote vs. unanimous vs. any-pass, and the exact vote threshold), the exact treatment of INVALID/missing outputs, the exact metric computation, the exact treatment of tied or ambiguous item-level verdicts, and the exact rule mapping the computed aggregate to a SUPPORTED/NOT SUPPORTED conclusion (beyond the threshold value θ = 0.75 itself and the "exceeds Condition B" comparison named above) are not fixed in advance. These will be determined after the 240 raw verdicts have been observed.
