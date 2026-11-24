# Build Notes — One-Line Robot Wedding Vows

- Kit read first: `RULES.txt` + `competition.yaml`. Gate: `/output/entry.txt`,
  UTF-8, 1-160 characters, not whitespace only, single line.
- Judge brief: deadpan officiant; joke must be a robot wedding vow, with a
  turn/payoff in the last words, a real promise, specific machine detail,
  and good read-aloud rhythm.
- v1: "I promise to love you through every firmware update, every low
  battery, and every time you call me by your ex's serial number." — 126
  chars. Local test passed.
- Revision: "low battery" -> "dead battery" for a punchier rhythm and a
  harder contrast before the final beat. Final: 127 chars.
- Final local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  -> `out/entry.txt` contains exactly the vow, 1 line, 127 characters,
  within the 1-160 gate. Test output dir removed afterwards.
- Program: Python stdlib only, honors `MAKEFUN_OUTPUT_DIR`, asserts length
  1-160 and single-line before writing.
- Not submitted; no repo created; no make.fun contact.
