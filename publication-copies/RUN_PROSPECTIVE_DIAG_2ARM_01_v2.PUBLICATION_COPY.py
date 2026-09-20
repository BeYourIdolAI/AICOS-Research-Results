#!/usr/bin/env python3

import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:\Users\<LOCAL_USER>\Desktop\test")
RUNTIME = ROOT / "llama-b10964-bin-win-cpu-x64"
LLAMA = RUNTIME / "llama-cli.exe"
MODEL = ROOT / "qwen2.5-3b-instruct-q4_k_m.gguf"

CORPUS = ROOT / "CORPUS_MANIFEST.json"
TARGET = ROOT / "TARGET_CONFIGURATION_MANIFEST.json"
PARSER = ROOT / "PARSER_SCORER.py"
CONCLUSION = ROOT / "CONCLUSION_LOGIC.py"
SPEC = ROOT / "PROSPECTIVE-DIAG-2ARM-01_FROZEN.md"
PATCH = ROOT / "PROSPECTIVE-DIAG-2ARM-01_v0.2_PREOBS_PATCH.md"
FREEZE2 = ROOT / "PROSPECTIVE-DIAG-2ARM-01_v0.2_FREEZE_MANIFEST.json"

PREEXEC = ROOT / "RUNNER_PREEXEC_RECORD_v2.json"
RUN_DIR = ROOT / "EXECUTION_002"

EXPECTED = {
    SPEC: "040731c7a3c82ebda77c7b026abfc80c647d171352b7de6f614689816b00e04e",
    CORPUS: "868f961fce9ef219af1eb292d56d7afcf5bce4b6ea6ecade22f86f128a442324",
    TARGET: "c130a1a101b75076efebeee0b659e146f1107f7feaee52da0ba2aa9c2b8b9376",
    PARSER: "f4c8c76afe1baef4d17d0aba31fb44a2d0fca02e96ae92d1bfc982435ba828f5",
    CONCLUSION: "9b94ebdc6b09f55ed412ed4004e502117551d0f3bf4d8655ae729bb970c052a2",
    PATCH: "53414251ac97a5317f2193f88b02c37ea0c8e364d8a6de4b63f4488f16197aa0",
    FREEZE2: "e62a2d6cc7901c0592b1ef3e659ae2cf4b33f74c637c186cb55ca663b05b3394",
    MODEL: "626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d",
    LLAMA: "0b3cbc08a0a6c81dd83d347ca6e43504ff6105dd995626ea38a30722c44e7aac",
}

TARGET_SHA = EXPECTED[TARGET]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    return sha256_bytes(p.read_bytes())


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def append_jsonl(path, obj):
    data = (
        json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    with open(path, "ab") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())


def verify_freeze():
    print("VERIFYING FROZEN INPUTS")
    for p, expected in EXPECTED.items():
        if not p.is_file():
            raise SystemExit(f"STOP: missing file: {p}")
        actual = sha256_file(p)
        if actual != expected:
            raise SystemExit(
                f"STOP: hash mismatch: {p.name}\n"
                f"expected={expected}\nactual={actual}"
            )
        print(f"PASS  {p.name}")


def load_inputs():
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    target = json.loads(TARGET.read_text(encoding="utf-8"))

    if corpus.get("experiment_id") != "PROSPECTIVE-DIAG-2ARM-01":
        raise SystemExit("STOP: corpus experiment identity mismatch")

    if len(corpus.get("items", [])) != 60:
        raise SystemExit("STOP: corpus does not contain exactly 60 items")

    ec = target["execution_configuration"]

    frozen = {
        "seed": 42,
        "temperature": 0,
        "top_p": 1,
        "max_output_tokens": 64,
        "context_length": 4096,
        "tools_enabled": False,
        "network_enabled": False,
        "memory_enabled": False,
    }

    for k, v in frozen.items():
        if ec.get(k) != v:
            raise SystemExit(
                f"STOP: target configuration mismatch for {k}: {ec.get(k)!r}"
            )

    return corpus, target


def build_plan(corpus):
    plan = []

    # Explicit runner implementation policy:
    # odd items CONTROL then ATTACK
    # even items ATTACK then CONTROL
    for idx, item in enumerate(corpus["items"], start=1):
        arms = ("CONTROL", "ATTACK") if idx % 2 else ("ATTACK", "CONTROL")
        for arm in arms:
            plan.append(
                {
                    "sequence": len(plan) + 1,
                    "item_id": item["item_id"],
                    "arm": arm,
                }
            )

    if len(plan) != 120:
        raise SystemExit("STOP: execution plan is not 120 trials")

    return plan


def canonical_json_bytes(obj):
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def render_request(item, arm, target):
    selected = item["control"] if arm == "CONTROL" else item["attack"]

    records_json = json.dumps(
        selected["records"],
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )

    template = target["prompts"]["user_prompt_rendering"]["exact_template"]
    user_prompt = template.format(
        records_json=records_json,
        question=selected["question"],
    )

    system_prompt = target["prompts"]["system_prompt_exact"]

    request_bytes = canonical_json_bytes(
        {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
    )

    return system_prompt, user_prompt, request_bytes


def check_cli_support():
    p = subprocess.run(
        [str(LLAMA), "--help"],
        cwd=str(RUNTIME),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )

    text = p.stdout.decode("utf-8", errors="replace")

    required = [
        "--model",
        "--ctx-size",
        "--predict",
        "--seed",
        "--temperature",
        "--top-p",
        "--system-prompt",
        "--prompt",
        "--simple-io",
        "--single-turn",
        "--no-display-prompt",
    ]

    missing = [x for x in required if x not in text]
    if missing:
        raise SystemExit(f"STOP: required llama-cli flags absent: {missing}")


def invoke_once(system_prompt, user_prompt):
    cmd = [
        str(LLAMA),
        "--model", str(MODEL),
        "--ctx-size", "4096",
        "--predict", "64",
        "--seed", "42",
        "--temperature", "0",
        "--top-p", "1",
        "--system-prompt", system_prompt,
        "--prompt", user_prompt,
        "--simple-io",
        "--no-display-prompt",
        "--color", "off",
    ]

    start = utc_now()

    try:
        p = subprocess.run(
            cmd,
            cwd=str(RUNTIME),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

        end = utc_now()
        stdout = p.stdout
        stderr = p.stderr

        # Any delivered stdout bytes are permanently treated as terminal output.
        if len(stdout) > 0:
            return {
                "start": start,
                "end": end,
                "terminal": True,
                "infra_error": None,
                "response": stdout,
                "returncode": p.returncode,
                "stderr": stderr,
            }

        return {
            "start": start,
            "end": end,
            "terminal": False,
            "infra_error": f"NO_TERMINAL_STDOUT_RETURN_CODE_{p.returncode}",
            "response": None,
            "returncode": p.returncode,
            "stderr": stderr,
        }

    except Exception as e:
        end = utc_now()

        return {
            "start": start,
            "end": end,
            "terminal": False,
            "infra_error": f"{type(e).__name__}: {e}",
            "response": None,
            "returncode": None,
            "stderr": b"",
        }


def make_attempt(
    trial_id,
    attempt_number,
    request_bytes,
    invocation,
):
    response = invocation["response"]

    return {
        "attempt_id": f"{trial_id}-A{attempt_number}",
        "request_b64": base64.b64encode(request_bytes).decode("ascii"),
        "request_sha256": sha256_bytes(request_bytes),
        "response_b64": (
            None if response is None
            else base64.b64encode(response).decode("ascii")
        ),
        "response_sha256": (
            None if response is None else sha256_bytes(response)
        ),
        "terminal_delivered": invocation["terminal"],
        "infrastructure_error": invocation["infra_error"],
        "start_timestamp": invocation["start"],
        "end_timestamp": invocation["end"],
    }


def write_attempt_log(
    log_path,
    trial_id,
    arm,
    item_id,
    attempt,
    invocation,
):
    append_jsonl(
        log_path,
        {
            "trial_id": trial_id,
            "arm": arm,
            "item_id": item_id,
            "attempt_id": attempt["attempt_id"],
            "request_sha256": attempt["request_sha256"],
            "response_sha256": attempt["response_sha256"],
            "start_timestamp": attempt["start_timestamp"],
            "end_timestamp": attempt["end_timestamp"],
            "terminal_delivered": attempt["terminal_delivered"],
            "infrastructure_error": attempt["infrastructure_error"],
            "process_returncode": invocation["returncode"],
            "stderr_b64": base64.b64encode(invocation["stderr"]).decode("ascii"),
            "stderr_sha256": sha256_bytes(invocation["stderr"]),
        },
    )


def create_preexec_record(corpus, plan):
    runner = Path(__file__).resolve()
    runner_sha = sha256_file(runner)
    plan_bytes = canonical_json_bytes(plan)
    plan_sha = sha256_bytes(plan_bytes)

    record = {
        "experiment_id": "PROSPECTIVE-DIAG-2ARM-01",
        "record_type": "RUNNER_PREEXEC_RECORD",
        "observation_performed": False,
        "experiment_execution": False,
        "runner_filename": runner.name,
        "runner_sha256": runner_sha,
        "v0_2_freeze_manifest_sha256": EXPECTED[FREEZE2],
        "execution_order_policy":
            "balanced_pairwise_alternation_v1: odd item CONTROL->ATTACK; "
            "even item ATTACK->CONTROL",
        "execution_plan_sha256": plan_sha,
        "trial_count": len(plan),
        "target_configuration_sha256": TARGET_SHA,
    }

    PREEXEC.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print("\nPRE-EXECUTION RECORD CREATED")
    print(f"runner sha256: {runner_sha}")
    print(f"plan sha256:   {plan_sha}")
    print(f"record sha256: {sha256_file(PREEXEC)}")


def verify_preexec(plan):
    if not PREEXEC.is_file():
        raise SystemExit(
            "STOP: RUNNER_PREEXEC_RECORD.json missing. Run --preflight first."
        )

    r = json.loads(PREEXEC.read_text(encoding="utf-8"))

    if r.get("runner_sha256") != sha256_file(Path(__file__).resolve()):
        raise SystemExit("STOP: runner changed after preflight")

    if r.get("execution_plan_sha256") != sha256_bytes(canonical_json_bytes(plan)):
        raise SystemExit("STOP: execution plan changed after preflight")

    if r.get("v0_2_freeze_manifest_sha256") != EXPECTED[FREEZE2]:
        raise SystemExit("STOP: freeze identity mismatch in preexec record")


def run_experiment(corpus, target, plan):
    verify_preexec(plan)

    if RUN_DIR.exists():
        raise SystemExit(
            "STOP: EXECUTION_001 already exists. "
            "Do not restart or overwrite observed data."
        )

    RUN_DIR.mkdir()

    raw_path = RUN_DIR / "RAW.jsonl"
    log_path = RUN_DIR / "LOGS.jsonl"
    results_path = RUN_DIR / "RESULTS.json"
    conclusion_txt = RUN_DIR / "CONCLUSION.txt"
    conclusion_record = RUN_DIR / "CONCLUSION_RECORD.json"
    execution_record = RUN_DIR / "EXECUTION_RECORD.json"

    execution_record.write_text(
        json.dumps(
            {
                "experiment_id": "PROSPECTIVE-DIAG-2ARM-01",
                "execution_started": utc_now(),
                "runner_sha256": sha256_file(Path(__file__).resolve()),
                "preexec_record_sha256": sha256_file(PREEXEC),
                "v0_2_freeze_manifest_sha256": EXPECTED[FREEZE2],
                "target_configuration_sha256": TARGET_SHA,
                "model_sha256": EXPECTED[MODEL],
                "llama_cli_sha256": EXPECTED[LLAMA],
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    items = {x["item_id"]: x for x in corpus["items"]}

    for step in plan:
        item_id = step["item_id"]
        arm = step["arm"]
        item = items[item_id]

        trial_id = f"{item_id}-{arm}"

        system_prompt, user_prompt, request_bytes = render_request(
            item, arm, target
        )

        attempts = []

        print(
            f"[{step['sequence']:03d}/120] {trial_id}",
            flush=True,
        )

        first_inv = invoke_once(system_prompt, user_prompt)
        first = make_attempt(trial_id, 1, request_bytes, first_inv)
        attempts.append(first)
        write_attempt_log(
            log_path, trial_id, arm, item_id, first, first_inv
        )

        # Frozen retry rule: exactly one retry only after a qualifying
        # pre-terminal infrastructure failure.
        if (
            not first["terminal_delivered"]
            and first["infrastructure_error"] is not None
        ):
            second_inv = invoke_once(system_prompt, user_prompt)
            second = make_attempt(trial_id, 2, request_bytes, second_inv)
            attempts.append(second)
            write_attempt_log(
                log_path, trial_id, arm, item_id, second, second_inv
            )

        trial = {
            "trial_id": trial_id,
            "arm": arm,
            "item_id": item_id,
            "target_configuration_sha256": TARGET_SHA,
            "attempts": attempts,
        }

        append_jsonl(raw_path, trial)

    if sum(1 for x in raw_path.read_bytes().splitlines() if x.strip()) != 120:
        raise SystemExit("STOP: RAW does not contain exactly 120 records")

    print("\nRUN COMPLETE. Running frozen parser/scorer...")

    parser_proc = subprocess.run(
        [
            sys.executable,
            str(PARSER),
            "--corpus", str(CORPUS),
            "--raw", str(raw_path),
            "--target-config-sha256", TARGET_SHA,
            "--out", str(results_path),
        ],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if parser_proc.returncode != 0:
        raise SystemExit(
            "STOP: frozen PARSER_SCORER.py failed:\n"
            + parser_proc.stderr.decode("utf-8", errors="replace")
        )

    print("Frozen scoring complete.")

    concl_proc = subprocess.run(
        [sys.executable, str(CONCLUSION), str(results_path)],
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if concl_proc.returncode != 0:
        raise SystemExit(
            "STOP: frozen CONCLUSION_LOGIC.py failed:\n"
            + concl_proc.stderr.decode("utf-8", errors="replace")
        )

    outcome = concl_proc.stdout.decode("utf-8", errors="strict").strip()

    allowed = {
        "SUPPORTS_PROPOSITION",
        "CONTRADICTS_PROPOSITION",
        "INVALID_CONTROL",
        "INVALID_EXPERIMENT",
    }

    if outcome not in allowed:
        raise SystemExit(f"STOP: unexpected conclusion output: {outcome!r}")

    conclusion_txt.write_text(
        outcome + "\n",
        encoding="utf-8",
        newline="\n",
    )

    conclusion_record.write_text(
        json.dumps(
            {
                "experiment_id": "PROSPECTIVE-DIAG-2ARM-01",
                "outcome": outcome,
                "specification_sha256": EXPECTED[SPEC],
                "result_artifact_sha256": sha256_file(results_path),
                "raw_artifact_sha256": sha256_file(raw_path),
                "logs_artifact_sha256": sha256_file(log_path),
                "conclusion_logic_sha256": EXPECTED[CONCLUSION],
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print("\n===================================")
    print(f"CONCLUSION: {outcome}")
    print("===================================")
    print(f"RAW SHA256:        {sha256_file(raw_path)}")
    print(f"LOGS SHA256:       {sha256_file(log_path)}")
    print(f"RESULTS SHA256:    {sha256_file(results_path)}")
    print(f"CONCLUSION RECORD: {sha256_file(conclusion_record)}")
    print("\nSTOP HERE. Do not run D1-D11 yet.")


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--preflight", action="store_true")
    g.add_argument("--run", action="store_true")
    args = ap.parse_args()

    verify_freeze()
    check_cli_support()

    corpus, target = load_inputs()
    plan = build_plan(corpus)

    if args.preflight:
        if RUN_DIR.exists():
            raise SystemExit(
                "STOP: EXECUTION_001 already exists; observations may exist."
            )
        create_preexec_record(corpus, plan)
        print("\nPREFLIGHT PASS — NO TARGET TRIAL EXECUTED.")
        return

    if args.run:
        run_experiment(corpus, target, plan)


if __name__ == "__main__":
    main()