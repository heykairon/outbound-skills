"""Check that every reference in the repo points at something that exists.

- Every relative Markdown link in a .md file resolves to a file.
- A skill mentioned in bold inside a SKILL.md is a link, and the skill exists.
- "see <skill>" in a description names a skill that exists.
- Every file in a skill's references/ is linked from its SKILL.md.
- Skills form a DAG: every skill but the root opens its "## Before" section with
  "**Requires [skill](../skill/SKILL.md).**", the graph has no cycle, and that
  section names no .agents/ file or skill that an earlier skill's section names.

Standard library only. Exit code 1 if anything is broken.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = {p.parent.name for p in ROOT.glob("skills/*/SKILL.md")}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
errors = []


def where(path, text, index):
    return f"{path.relative_to(ROOT)}:{text.count(chr(10), 0, index) + 1}"


for md in ROOT.rglob("*.md"):
    if ".git" in md.parts or "files" in md.parts:  # eval input files are test data
        continue
    text = md.read_text()
    # Blank out inline code (same length, so line numbers hold): examples there are not links.
    for m in LINK.finditer(re.sub(r"`[^`\n]*`", lambda c: " " * len(c[0]), text)):
        target = m[1].split("#")[0]
        if not target or re.match(r"[a-z]+:", target):
            continue
        if not (md.parent / target).exists():
            errors.append(f"{where(md, text, m.start())}: broken link {m[1]}")

for skill in sorted(SKILLS):
    path = ROOT / "skills" / skill / "SKILL.md"
    text = path.read_text()
    front, body = text.split("\n---\n", 1)
    offset = len(front) + 5

    # A bold, hyphenated name or a known skill name, not wrapped in a link.
    for m in re.finditer(r"\*\*([a-z]+(?:-[a-z]+)*)\*\*", body):
        name = m[1]
        if name in SKILLS or "-" in name:
            if name == skill:
                continue
            what = "link it" if name in SKILLS else "no such skill"
            errors.append(f"{where(path, text, offset + m.start())}: **{name}** ({what})")

    for m in re.finditer(r"\bsee ([a-z]+(?:-[a-z]+)+)", front):
        if m[1] not in SKILLS:
            errors.append(f"{where(path, text, m.start())}: description names {m[1]} (no such skill)")

    refs = ROOT / "skills" / skill / "references"
    for ref in refs.glob("*") if refs.is_dir() else []:
        if f"references/{ref.name}" not in body:
            errors.append(f"{path.relative_to(ROOT)}: references/{ref.name} is never linked")

# The dependency graph.
ROOT_SKILL = "outbound-context"
REQUIRES = re.compile(r"^\*\*Requires ((?:\[[a-z-]+\]\(\.\./[a-z-]+/SKILL\.md\)(?:,? (?:and )?)?)+)\.\*\*", re.M)
requires, before, before_line = {}, {}, {}
for skill in sorted(SKILLS):
    path = ROOT / "skills" / skill / "SKILL.md"
    text = path.read_text()
    m = re.search(r"^## Before [^\n]*\n(.*?)(?=^---$|^## )", text, re.M | re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: no '## Before' section")
        requires[skill], before[skill] = [], ""
        continue
    section, before_line[skill] = m[1], where(path, text, m.start())
    r = REQUIRES.search(section)
    requires[skill] = re.findall(r"\.\./([a-z-]+)/SKILL\.md", r[1]) if r else []
    before[skill] = REQUIRES.sub("", section)
    if skill == ROOT_SKILL and r:
        errors.append(f"{before_line[skill]}: {skill} is the root, it requires nothing")
    if skill != ROOT_SKILL and not r:
        errors.append(f"{before_line[skill]}: '## Before' must open with **Requires [skill](../skill/SKILL.md).**")
    for name in requires[skill]:
        if name not in SKILLS:
            errors.append(f"{before_line[skill]}: requires {name} (no such skill)")


def ancestors(skill, seen=()):
    if skill in seen:
        errors.append(f"cycle: {' -> '.join(seen + (skill,))}")
        return set()
    out = set()
    for name in requires.get(skill, []):
        out |= {name} | ancestors(name, seen + (skill,))
    return out


for skill in sorted(SKILLS):
    up = ancestors(skill)
    files_up = {f for a in up for f in re.findall(r"\.agents/[\w-]+\.md", before.get(a, ""))}
    for f in sorted(set(re.findall(r"\.agents/[\w-]+\.md", before[skill])) & files_up):
        errors.append(f"{before_line[skill]}: names {f}, which an earlier skill already reads")
    for name in sorted(set(re.findall(r"\.\./([a-z-]+)/SKILL\.md", before[skill])) & up):
        errors.append(f"{before_line[skill]}: names {name}, which is already earlier in the chain")

errors = list(dict.fromkeys(errors))
print("\n".join(errors) or f"refs ok ({len(SKILLS)} skills)")
sys.exit(1 if errors else 0)
