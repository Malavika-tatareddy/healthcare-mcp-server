import os
import re
from pathlib import Path
from mcp.server.fastmcp import FastMCP

NOTES_FILE = Path(__file__).parent / "US Healthcare Domain Notes.md"

mcp = FastMCP(
    "Healthcare Notes Server",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)),
)


def load_terms():
    terms = {}
    tips = []
    text = NOTES_FILE.read_text()

    for raw_line in text.splitlines():
        line = raw_line.strip()

        tip_match = re.match(r"\*\*Interview tip:\*\*\s*(.+)$", line)
        if tip_match:
            tips.append(tip_match.group(1))
            continue

        # Table rows, e.g. "| **Term** | Full Form | Meaning |"
        if line.startswith("|") and "**" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            term_match = re.match(r"\*\*(.+?)\*\*", cells[0])
            if term_match and len(cells) >= 2:
                _store_term(terms, term_match.group(1), cells[-1])
            continue

        # Bullet points, e.g. "- **Term** (extra) — meaning"
        bullet_match = re.match(r"-\s*\*\*(.+?)\*\*\s*(?:\(.*?\))?\s*—\s*(.+)$", line)
        if bullet_match:
            _store_term(terms, bullet_match.group(1), bullet_match.group(2))
            continue

        # Standalone definitions, e.g. "**Term** (extra) = meaning"
        equals_match = re.match(r"\*\*(.+?)\*\*\s*(?:\(.*?\))?\s*=\s*(.+)$", line)
        if equals_match:
            _store_term(terms, equals_match.group(1), equals_match.group(2))

    return terms, tips


def _store_term(terms, term, meaning):
    terms[term.strip().lower()] = meaning.strip()
    if "/" in term:
        for part in term.split("/"):
            terms.setdefault(part.strip().lower(), meaning.strip())


@mcp.prompt()
def quiz_me() -> str:
    """A ready-made instruction that asks the AI to quiz the user on a random US Healthcare term."""
    return (
        "Pick one random US Healthcare vocabulary term from the notes resource "
        "(healthcare://notes), ask me what it means, wait for my answer, "
        "then tell me if I was right and give the correct definition."
    )


@mcp.resource("healthcare://notes")
def healthcare_notes() -> str:
    """Return the full US Healthcare domain notes, as raw text."""
    return NOTES_FILE.read_text()


@mcp.tool()
def get_healthcare_term(term: str) -> str:
    """Look up any US Healthcare term from the full notes and return its meaning, plus a related interview tip if one exists."""
    terms, tips = load_terms()
    meaning = terms.get(term.strip().lower())
    if not meaning:
        return f"Sorry, I don't have a definition for '{term}' yet."

    result = f"{term}: {meaning}"
    related_tip = next((tip for tip in tips if term.strip().lower() in tip.lower()), None)
    if related_tip:
        result += f"\n\nInterview tip: {related_tip}"
    return result


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
