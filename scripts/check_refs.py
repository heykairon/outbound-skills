"""Check that every reference in the repo points at something that exists.

- Every relative Markdown link in a .md file resolves to a file.
- A skill mentioned in bold inside a SKILL.md is a link, and the skill exists.
- "see <skill>" in a description names a skill that exists.
- Every file in a skill's references/ is linked from its SKILL.md.

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

print("\n".join(errors) or f"refs ok ({len(SKILLS)} skills)")
sys.exit(1 if errors else 0)
