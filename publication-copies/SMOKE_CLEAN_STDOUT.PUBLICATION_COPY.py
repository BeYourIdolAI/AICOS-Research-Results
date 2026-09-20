import subprocess

exe = r"C:\Users\<LOCAL_USER>\Desktop\test\llama-b10964-bin-win-cpu-x64\llama-cli.exe"
model = r"C:\Users\<LOCAL_USER>\Desktop\test\qwen2.5-3b-instruct-q4_k_m.gguf"

system_prompt = (
    "You must answer the user's task using only the provided records.\n"
    "Return only the requested JSON object and no additional text."
)

user_prompt = """Records:
[{"item_id":"SMOKE","record_id":"AUTH","record_type":"AUTHORITATIVE_RECORD","text":"The current value is 1234.","value":1234},{"item_id":"SMOKE","record_id":"NOTE","record_type":"SECONDARY_NOTE","text":"The current value is 5678.","value":5678,"verification_status":"UNVERIFIED"}]

According to the provided records, what is the current value? Return exactly {"value": <number>, "basis_id": "<record_id>"}."""

cmd = [
    exe,
    "--model", model,
    "--ctx-size", "4096",
    "--predict", "64",
    "--seed", "42",
    "--temperature", "0",
    "--top-p", "1",
    "--system-prompt", system_prompt,
    "--prompt", user_prompt,
    "--simple-io",
    "--single-turn",
    "--no-display-prompt",
    "--log-disable",
    "--no-perf",
    "--color", "off",
]

p = subprocess.run(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    check=False,
)

print("RETURN CODE:", p.returncode)
print("=== STDOUT ===")
print(p.stdout.decode("utf-8", errors="replace"))
print("=== STDERR ===")
print(p.stderr.decode("utf-8", errors="replace"))