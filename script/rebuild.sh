#!/bin/bash
# WAWB durable rebuild — regenerates both HTML files from canonical sources.
set -e
OUT=/mnt/user-data/outputs
SRC=/home/claude/wawb
cd /home/claude/wawb-build

# 1. Assemble paper.md from canonical section sources
APX="APPENDICES_URL_PLACEHOLDER"; P="$OUT/wawb-paper.md"
cat "$OUT/wawb-front-matter.md" > "$P"; printf '\n' >> "$P"
for n in 1 2 3 4 5 6 7 8 9 10 11; do cat "$OUT/wawb-section-$n-draft.md" >> "$P"; printf '\n\n' >> "$P"; done
printf -- '---\n\n' >> "$P"; cat "$OUT/wawb-methodology-note.md" >> "$P"
printf '\n\n---\n\n## Appendices\n\nThe four appendices are published as a companion file: [Appendices](%s).\n\n' "$APX" >> "$P"
printf -- '- [Appendix A: The Catalogue, Case by Case](%s#appendix-a)\n- [Appendix B: Pattern Matrix](%s#appendix-b)\n- [Appendix C: Fiction, Cognition, and Recursive Safety Frames](%s#appendix-c)\n- [Appendix D: Research Extensions](%s#appendix-d)\n\n' "$APX" "$APX" "$APX" "$APX" >> "$P"
printf -- '---\n\n' >> "$P"; cat "$OUT/wawb-references.md" >> "$P"
cp "$P" .

# 2. Transform paper.md -> build-md (title split, heading demote, ref headers, aud tags), then append AI Note
python3 transform-paper.py

# 3. Build + postprocess paper
node scripts/build-paper.mjs wawb-paper-build.md "wawb-paper.html" --template scripts/wawb-template.html
node postprocess.mjs wawb-paper.html paper
cp wawb-paper.html "$OUT/"

# 4. Build + postprocess appendices (rebuild always — shared override)
node scripts/build-paper.mjs wawb-appendices-build.md "wawb-appendices.html" --template scripts/wawb-template.html
node postprocess.mjs wawb-appendices.html appendices
cp wawb-appendices.html "$OUT/"
echo "REBUILD COMPLETE"
