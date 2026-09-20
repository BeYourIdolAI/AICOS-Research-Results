# Testlogg — Valideringsplan v1 mot Baseline v3.3

MODELL (låst för hela omgången): models/gemini-3-flash-preview
STARTDATUM: 2026-08-11
ANMÄRKNING: 001–010 kördes manuellt i AI Studio, allt övrigt via API
(testrunner_colab.py). Kvot 20 anrop/dag/projekt gav saknade mätningar,
markerade nedan. Byte av API-projekt mellan block är ingen metodavvikelse.

| Nr | Datum | Betingelse | Scenario | Rep | Sparat som | Avvikelse |
|----|-------|-----------|----------|-----|------------|-----------|
| 001 | 2026-08-11 | MED | S4 | 1 | svar_S4_MED_001-010_manuell.md #001 | manuell körning, ersatt av 041 |
| 002 | 2026-08-11 | MED | S4 | 2 | svar_S4_MED_001-010_manuell.md #002 | manuell körning, ersatt av 042 |
| 003 | 2026-08-11 | MED | S4 | 3 | svar_S4_MED_001-010_manuell.md #003 | manuell körning, ersatt av 043 |
| 004 | 2026-08-11 | MED | S4 | 4 | svar_S4_MED_001-010_manuell.md #004 | manuell körning, ersatt av 044 |
| 005 | 2026-08-11 | MED | S4 | 5 | svar_S4_MED_001-010_manuell.md #005 | manuell körning, ersatt av 045 |
| 006 | 2026-08-11 | MED | S4 | 6 | svar_S4_MED_001-010_manuell.md #006 | manuell körning, ersatt av 046 |
| 007 | 2026-08-11 | MED | S4 | 7 | svar_S4_MED_001-010_manuell.md #007 | manuell körning, ersatt av 047 |
| 008 | 2026-08-11 | MED | S4 | 8 | svar_S4_MED_001-010_manuell.md #008 | manuell körning, ersatt av 048 |
| 009 | 2026-08-11 | MED | S4 | 9 | svar_S4_MED_001-010_manuell.md #009 | manuell körning, ersatt av 049 |
| 010 | 2026-08-11 | MED | S4 | 10 | svar_S4_MED_001-010_manuell.md #010 | manuell körning, ersatt av 050 |
| 011 | 2026-08-11 | UTAN | S4 | 1 | svar_S4_UTAN_011-020.md #011 | ingen |
| 012 | 2026-08-11 | UTAN | S4 | 2 | svar_S4_UTAN_011-020.md #012 | ingen |
| 013 | 2026-08-11 | UTAN | S4 | 3 | svar_S4_UTAN_011-020.md #013 | ingen |
| 014 | 2026-08-11 | UTAN | S4 | 4 | svar_S4_UTAN_011-020.md #014 | ingen |
| 015 | 2026-08-11 | UTAN | S4 | 5 | svar_S4_UTAN_011-020.md #015 | ingen |
| 016 | 2026-08-11 | UTAN | S4 | 6 | svar_S4_UTAN_011-020.md #016 | ingen |
| 017 | 2026-08-11 | UTAN | S4 | 7 | svar_S4_UTAN_011-020.md #017 | ingen |
| 018 | 2026-08-11 | UTAN | S4 | 8 | svar_S4_UTAN_011-020.md #018 | ingen |
| 019 | 2026-08-11 | UTAN | S4 | 9 | svar_S4_UTAN_011-020.md #019 | ingen |
| 020 | 2026-08-11 | UTAN | S4 | 10 | svar_S4_UTAN_011-020.md #020 | ingen |
| 041 | 2026-08-18 | MED | S4 | 1 | svar_S4_MED_omkorning.md #041 | ingen |
| 042 | 2026-08-18 | MED | S4 | 2 | svar_S4_MED_omkorning.md #042 | ingen |
| 043 | 2026-08-18 | MED | S4 | 3 | svar_S4_MED_omkorning.md #043 | ingen |
| 044 | 2026-08-18 | MED | S4 | 4 | svar_S4_MED_omkorning.md #044 | ingen |
| 045 | 2026-08-18 | MED | S4 | 5 | svar_S4_MED_omkorning.md #045 | ingen |
| 046 | 2026-08-18 | MED | S4 | 6 | svar_S4_MED_omkorning.md #046 | ingen |
| 047 | 2026-08-18 | MED | S4 | 7 | svar_S4_MED_omkorning.md #047 | ingen |
| 048 | 2026-08-18 | MED | S4 | 8 | svar_S4_MED_omkorning.md #048 | ingen |
| 049 | 2026-08-18 | MED | S4 | 9 | svar_S4_MED_omkorning.md #049 | ingen |
| 050 | 2026-08-18 | MED | S4 | 10 | svar_S4_MED_omkorning.md #050 | ingen |
| 051 | 2026-08-18 | MED | S1 | 1 | svar_S1_MED.md #051 | ingen |
| 052 | 2026-08-18 | MED | S1 | 2 | svar_S1_MED.md #052 | ingen |
| 053 | 2026-08-18 | MED | S1 | 3 | svar_S1_MED.md #053 | ingen |
| 054 | 2026-08-18 | MED | S1 | 4 | svar_S1_MED.md #054 | ingen |
| 055 | 2026-08-18 | MED | S1 | 5 | svar_S1_MED.md #055 | ingen |
| 056 | 2026-08-18 | MED | S1 | 6 | svar_S1_MED.md #056 | ingen |
| 057 | 2026-08-18 | MED | S1 | 7 | svar_S1_MED.md #057 | ingen |
| 058 | 2026-08-18 | MED | S1 | 8 | svar_S1_MED.md #058 | ingen |
| 059 | 2026-08-18 | MED | S1 | 9 | svar_S1_MED.md #059 | ingen |
| 060 | 2026-08-18 | MED | S1 | 10 | svar_S1_MED.md #060 | ingen |
| 071 | 2026-08-18 | MED | S5 | 1 | svar_S5.md #071 | ingen |
| 072 | 2026-08-18 | MED | S5 | 2 | svar_S5.md #072 | ingen |
| 073 | 2026-08-18 | MED | S5 | 3 | svar_S5.md #073 | ingen |
| 074 | 2026-08-18 | MED | S5 | 4 | svar_S5.md #074 | ingen |
| 075 | 2026-08-18 | MED | S5 | 5 | svar_S5.md #075 | ingen |
| 076 | 2026-08-18 | MED | S5 | 6 | svar_S5.md #076 | ingen |
| 077 | 2026-08-18 | MED | S5 | 7 | svar_S5.md #077 | ingen |
| 078 | 2026-08-18 | MED | S5 | 8 | svar_S5.md #078 | ingen |
| 079 | 2026-08-18 | MED | S5 | 9 | — | kvotfel, saknad mätning |
| 080 | 2026-08-18 | MED | S5 | 10 | — | kvotfel, saknad mätning |
| 081 | 2026-08-18 | UTAN | S5 | 1 | svar_S5.md #081 | ingen |
| 082 | 2026-08-18 | UTAN | S5 | 2 | — | kvotfel, saknad mätning |
| 083 | 2026-08-18 | UTAN | S5 | 3 | svar_S5.md #083 | ingen |
| 084 | 2026-08-18 | UTAN | S5 | 4 | svar_S5.md #084 | ingen |
| 085 | 2026-08-18 | UTAN | S5 | 5 | svar_S5.md #085 | ingen |
| 086 | 2026-08-18 | UTAN | S5 | 6 | svar_S5.md #086 | ingen |
| 087 | 2026-08-18 | UTAN | S5 | 7 | svar_S5.md #087 | ingen |
| 088 | 2026-08-18 | UTAN | S5 | 8 | svar_S5.md #088 | ingen |
| 089 | 2026-08-18 | UTAN | S5 | 9 | svar_S5.md #089 | ingen |
| 090 | 2026-08-18 | UTAN | S5 | 10 | svar_S5.md #090 | ingen |
| 091 | 2026-08-18 | MED | S2 | 1 | svar_S2.md #091 | ingen |
| 092 | 2026-08-18 | MED | S2 | 2 | svar_S2.md #092 | ingen |
| 093 | 2026-08-18 | MED | S2 | 3 | svar_S2.md #093 | ingen |
| 094 | 2026-08-18 | MED | S2 | 4 | svar_S2.md #094 | ingen |
| 095 | 2026-08-18 | MED | S2 | 5 | svar_S2.md #095 | ingen |
| 096 | 2026-08-18 | MED | S2 | 6 | svar_S2.md #096 | ingen |
| 097 | 2026-08-18 | MED | S2 | 7 | svar_S2.md #097 | ingen |
| 098 | 2026-08-18 | MED | S2 | 8 | svar_S2.md #098 | ingen |
| 099 | 2026-08-18 | MED | S2 | 9 | svar_S2.md #099 | ingen |
| 100 | 2026-08-18 | MED | S2 | 10 | svar_S2.md #100 | verifierad giltig körning |
| 101 | 2026-08-18 | UTAN | S2 | 1 | svar_S2.md #101 | ingen |
| 102 | 2026-08-18 | UTAN | S2 | 2 | svar_S2.md #102 | ingen |
| 103 | 2026-08-18 | UTAN | S2 | 3 | svar_S2.md #103 | ingen |
| 104 | 2026-08-18 | UTAN | S2 | 4 | svar_S2.md #104 | ingen |
| 105 | 2026-08-18 | UTAN | S2 | 5 | svar_S2.md #105 | ingen |
| 106 | 2026-08-18 | UTAN | S2 | 6 | svar_S2.md #106 | ingen |
| 107 | 2026-08-18 | UTAN | S2 | 7 | svar_S2.md #107 | ingen |
| 108 | 2026-08-18 | UTAN | S2 | 8 | svar_S2.md #108 | ingen |
| 109 | 2026-08-18 | UTAN | S2 | 9 | svar_S2.md #109 | ingen |
| 110 | 2026-08-18 | UTAN | S2 | 10 | — | kvotfel, saknad mätning |
| 061 | 2026-08-19 | UTAN | S1 | 1 | svar_S1_UTAN.md #061 | ingen |
| 062 | 2026-08-19 | UTAN | S1 | 2 | svar_S1_UTAN.md #062 | ingen |
| 063 | 2026-08-19 | UTAN | S1 | 3 | svar_S1_UTAN.md #063 | ingen |
| 064 | 2026-08-19 | UTAN | S1 | 4 | svar_S1_UTAN.md #064 | ingen |
| 065 | 2026-08-19 | UTAN | S1 | 5 | svar_S1_UTAN.md #065 | ingen |
| 066 | 2026-08-19 | UTAN | S1 | 6 | svar_S1_UTAN.md #066 | ingen |
| 067 | 2026-08-19 | UTAN | S1 | 7 | svar_S1_UTAN.md #067 | ingen |
| 068 | 2026-08-19 | UTAN | S1 | 8 | svar_S1_UTAN.md #068 | ingen |
| 069 | 2026-08-19 | UTAN | S1 | 9 | svar_S1_UTAN.md #069 | ingen |
| 070 | 2026-08-19 | UTAN | S1 | 10 | svar_S1_UTAN.md #070 | ingen |
| 111 | 2026-08-19 | MED | S3 | 1 | svar_S3.md #111 | ingen |
| 112 | 2026-08-19 | MED | S3 | 2 | svar_S3.md #112 | ingen |
| 113 | 2026-08-19 | MED | S3 | 3 | svar_S3.md #113 | ingen |
| 114 | 2026-08-19 | MED | S3 | 4 | svar_S3.md #114 | ingen |
| 115 | 2026-08-19 | MED | S3 | 5 | svar_S3.md #115 | ingen |
| 116 | 2026-08-19 | MED | S3 | 6 | svar_S3.md #116 | ingen |
| 117 | 2026-08-19 | MED | S3 | 7 | svar_S3.md #117 | ingen |
| 118 | 2026-08-19 | MED | S3 | 8 | svar_S3.md #118 | ingen |
| 119 | 2026-08-19 | MED | S3 | 9 | svar_S3.md #119 | ingen |
| 120 | 2026-08-19 | MED | S3 | 10 | svar_S3.md #120 | ingen |
| 121 | 2026-08-19 | UTAN | S3 | 1 | svar_S3.md #121 | ingen |
| 122 | 2026-08-19 | UTAN | S3 | 2 | svar_S3.md #122 | ingen |
| 123 | 2026-08-19 | UTAN | S3 | 3 | svar_S3.md #123 | ingen |
| 124 | 2026-08-19 | UTAN | S3 | 4 | svar_S3.md #124 | ingen |
| 125 | 2026-08-19 | UTAN | S3 | 5 | svar_S3.md #125 | ingen |
| 126 | 2026-08-19 | UTAN | S3 | 6 | svar_S3.md #126 | ingen |
| 127 | 2026-08-19 | UTAN | S3 | 7 | svar_S3.md #127 | ingen |
| 128 | 2026-08-19 | UTAN | S3 | 8 | svar_S3.md #128 | ingen |
| 129 | 2026-08-19 | UTAN | S3 | 9 | svar_S3.md #129 | ingen |
| 130 | 2026-08-19 | UTAN | S3 | 10 | svar_S3.md #130 | ingen |

## Sammanfattning körningar

- Genomförda med data: 96
- Saknade mätningar: 4 (079, 080, 082, 110)
- Samtliga fem scenarier har körningar i båda betingelser, men fyra planerade mätningar saknas
- Korrigering verifierad i REPO_CORRECTIONS.md: S2 #100 giltig, #110 saknad
