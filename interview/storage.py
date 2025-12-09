from pathlib import Path
from datetime import datetime
from typing import List, Dict

DATA_DIR = Path("data")
HISTORY_FILE = DATA_DIR / "answers.txt"


def save_answer(role: str, question: str, answer: str) -> None:
    # Append the Q&A to a simple text file for now.
    DATA_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().isoformat(timespec="seconds")

    with HISTORY_FILE.open("a", encoding="utf-8") as f:
        f.write(f"--- {timestamp} ---\n")
        f.write(f"Role: {role}\n")
        f.write(f"Q: {question}\n")
        f.write(f"A: {answer}\n\n")


def load_recent_answers(limit: int = 5) -> List[Dict[str, str]]:
    if not HISTORY_FILE.exists():
        return []

    entries: List[Dict[str, str]] = []
    current: Dict[str, str] = {}

    with HISTORY_FILE.open("r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")

            if line.startswith("--- ") and line.endswith(" ---"):
                # start of a new entry
                if current:
                    entries.append(current)
                    current = {}

                # strip the leading/trailing dashes and spaces to keep just the timestamp
                current["timestamp"] = line.strip("- ").strip()
            elif line.startswith("Role: "):
                current["role"] = line[len("Role: "):].strip()
            elif line.startswith("Q: "):
                current["question"] = line[len("Q: "):].strip()
            elif line.startswith("A: "):
                current["answer"] = line[len("A: "):].strip()
            else:
                # blank lines or anything else can be ignored
                continue

    # append the last one if present
    if current:
        entries.append(current)

    # return most recent first
    return list(reversed(entries))[:limit]
