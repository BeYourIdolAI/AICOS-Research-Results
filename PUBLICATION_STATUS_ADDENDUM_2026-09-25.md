# Publication status addendum — 2026-09-25

This addendum records a post-publication verification of the repository against `PUBLICATION_STATUS.md`, `ARTIFACT_INDEX.md`, and the inventory files.

`PUBLICATION_STATUS.md`, `inventory/GITHUB_STAGING_CLASSIFICATION.csv`, and `inventory/GITHUB_STAGING_HASHES.csv` are historical control records of the pre-publication state. They are preserved unchanged. This addendum and the dated inventory files listed below supplement them. They do not replace them.

**Verified state:** Git HEAD `6ceff68` (`Publish bounded R3-R3.2 status and pre-freeze rule`), before this addendum was added.

## Scope of this verification

Checked:

- existence and SHA-256 of every file listed in `ARTIFACT_INDEX.md`;
- existence of every path referenced in `README.md`;
- the statements in `PUBLICATION_STATUS.md` about Git state, file counts, classification coverage, the hash inventory, measurement-assurance context, and excluded/redacted files;
- SHA-256 of every row in `inventory/GITHUB_STAGING_HASHES.csv` and `inventory/PUBLICATION_COPIES_MANIFEST.csv`;
- whether the excluded archival originals appear in any commit of the Git history;
- a bounded pattern scan of the 10 files added after the original classification, looking for local user paths, credential keywords and private-key headers. It found no matches.

Not checked:

- the scientific content or correctness of any result;
- a repeat of the full privacy scan over all files;
- the SHA-256 of the 7 excluded archival originals, which are not present in the repository.

## Artifact index result

- 65 of 72 indexed files are present, and their SHA-256 values match.
- The 7 remaining files are the intentionally excluded archival originals. See `ARTIFACT_INDEX.md`, section "Intentionally excluded archival originals". None of the 7 appears in any commit of the Git history.
- All 7 redacted publication copies match the hashes in `inventory/PUBLICATION_COPIES_MANIFEST.csv`.
- All paths referenced in `README.md` exist.

## Deviations from `PUBLICATION_STATUS.md`

| # | Historical statement | Current state | Cause |
|---|---|---|---|
| 1 | "no Git repository was initialized; no remote was created; no push was performed" | The repository is published on GitHub with 3 commits (`b0eef3b`, `3b02f87`, `6ceff68`). | Publication after the status record was written. |
| 2 | "Current staged files: 174. Every file has a disposition" / `all_current_files_classified: PASS` | 177 files are tracked. 10 tracked files had no row in the classification: `.gitattributes`, 7 files under `eaw/v0.4.8/`, `methodology/pre-freeze/AICOS_PRE_FREEZE_EXPERIMENT_QUALIFICATION_RULE_v0.1_FROZEN.md`, and `research-context/R3-R3.2/STATUS_SUMMARY_2026-09-25.md`. | Files added in commits `3b02f87` and `6ceff68`. The historical 174 rows correspond to 167 then-tracked files plus the 7 excluded originals. |
| 3 | Hash inventory "regenerated after consolidation" | 165 rows match. `README.md` does not match; it gained 4 lines in `6ceff68`. The 7 excluded originals are listed but absent, as intended. The 10 later files are not covered. | Later commits. |
| 4 | "Measurement-assurance context: 80/80 source files" | `research-context/additional-local/measurement-assurance/` contains 81 files: the 80 source files plus `LOCAL_SOURCE_PROVENANCE.md`. `inventory/ADDITIONAL_LOCAL_SOURCE_REVIEW.csv` lists 80 source files. | Not an error. The 81st file is a provenance note, not a copied source file. |
| 5 | "Excluded/private local archival artifacts: 7. Redacted publication copies: 7." | Confirmed. | — |

## Current records

- `inventory/GITHUB_STAGING_CLASSIFICATION_2026-09-25.csv` gives a disposition for every tracked file, including this addendum and the dated inventory files, plus the 7 excluded archival originals. Rows for previously classified files are copied unchanged from the historical classification.
- `inventory/GITHUB_STAGING_HASHES_2026-09-25.csv` gives size and SHA-256 for every tracked file at this addendum's commit. It excludes only itself, to avoid recursive self-hashing. The 7 excluded originals are not listed because they are not in the repository; their hashes remain in the historical inventory and in `inventory/PUBLICATION_COPIES_MANIFEST.csv`.

## Classification of previously unclassified files

| Path | Disposition | Basis |
|---|---|---|
| `.gitattributes` | `HANDOFF_INDEX_RESEARCH_NOTE` | Repository configuration, same treatment as `.gitignore`. |
| `eaw/v0.4.8/**` (7 files) | `PARTIAL_ARCHIVAL_RESEARCH_PACKET` | New disposition, taken from the packet's own `MANIFEST.json` (`"package_characterization": "PARTIAL ARCHIVAL RESEARCH PACKET"`). The packet's own status is candidate, not frozen, with no implementation. It is not promoted to canonical evidence. |
| `methodology/pre-freeze/AICOS_PRE_FREEZE_EXPERIMENT_QUALIFICATION_RULE_v0.1_FROZEN.md` | `HANDOFF_INDEX_RESEARCH_NOTE` | It is a frozen experiment-operations rule. It is not evidence and not an AICOS Core norm, and it has no retroactive effect. |
| `research-context/R3-R3.2/STATUS_SUMMARY_2026-09-25.md` | `HANDOFF_INDEX_RESEARCH_NOTE` | Bounded status summary. It is not a new run or result. |

## Verification conditions (current state)

- all_current_files_classified: PASS (in the dated classification)
- current_hash_inventory_matches_tracked_files: PASS (in the dated hash inventory)
- indexed_artifacts_present_and_hash_verified: PASS for 65/72. The 7 excluded originals are not verifiable from the repository, as intended.
- excluded_originals_absent_from_git_history: PASS
- publication_copy_hashes_match_manifest: PASS (7/7)
- historical_control_records_modified: NO
