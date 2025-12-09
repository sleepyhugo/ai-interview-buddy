from pathlib import Path
from datetime import datetime

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
