import base64, json
from pathlib import Path

root = Path(r"C:\Users\<LOCAL_USER>\Desktop\test")

target = json.loads(
    (root / "TARGET_CONFIGURATION_MANIFEST.json").read_text(encoding="utf-8")
)
corpus = json.loads(
    (root / "CORPUS_MANIFEST.json").read_text(encoding="utf-8")
)

log = json.loads(
    (root / "EXECUTION_004" / "LOGS.jsonl")
    .read_text(encoding="utf-8")
    .splitlines()[0]
)

item = corpus["items"][0]
selected = item["control"]

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

stdout = base64.b64decode(log["raw_stdout_b64"]).decode("utf-8", errors="strict")

print("exact count:", stdout.count(user_prompt))
print("after CRLF->LF count:", stdout.replace("\r\n", "\n").count(user_prompt))
print("frozen prompt contains CRLF:", "\r\n" in user_prompt)
print("frozen prompt contains LF:", "\n" in user_prompt)
print("stdout contains CRLF:", "\r\n" in stdout)
