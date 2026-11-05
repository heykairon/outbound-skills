#!/usr/bin/env bash
# Lint every skill: the official Agent Skills validator, then our reference check.
# Install the validator (Python 3.11+):
#   pip install 'git+https://github.com/agentskills/agentskills#subdirectory=skills-ref'
set -euo pipefail
cd "$(dirname "$0")/.."

if command -v skills-ref >/dev/null; then
  for d in skills/*/; do skills-ref validate "$d"; done
else
  # ponytail: without skills-ref, check the YAML, the name and the description length only.
  echo "skills-ref not installed: checking YAML, name and description length only"
  for f in skills/*/SKILL.md; do
    ruby -ryaml -e '
      d = YAML.safe_load(File.read(ARGV[0]).split(/^---$/)[1])
      abort "name is not the folder name" unless d["name"] == File.basename(File.dirname(ARGV[0]))
      abort "description is over 1024 characters" unless d["description"].to_s.size.between?(1, 1024)
    ' "$f" || { echo "failed: $f"; exit 1; }
  done
fi

python3 scripts/check_refs.py
