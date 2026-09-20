# Runtime provenance

The model binary and llama.cpp binary bundle are intentionally excluded from Git staging. `RUNTIME_BUNDLE_HASHES.csv` and frozen target-configuration manifests preserve locally evidenced identities.

Locally evidenced target configuration identifies `qwen2.5-3b-instruct-q4_k_m.gguf` with SHA-256 `626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d`, and `llama-cli.exe` with SHA-256 `0b3cbc08a0a6c81dd83d347ca6e43504ff6105dd995626ea38a30722c44e7aac`. The target manifest records runtime version `0.4.1-dev`, build `10964`, commit `b29c606e2`, on Windows x86_64. No download URL is asserted here.
