from typing import Dict, List

# Some simple heuristics to judge the answer
ACTION_VERBS = [
    "designed", "built", "implemented", "debugged", "fixed", "led",
    "optimized", "tested", "collaborated", "improved", "created",
    "automated", "refactored",
]

FILLER_PHRASES = [
    "um", "uh", "like", "you know", "kind of", "sort of", "basically",
]


def evaluate_answer(answer: str) -> Dict[str, object]:

    feedback: List[str] = []

    stripped = answer.strip()
    if not stripped:
        return {
            "word_count": 0,
            "filler_count": 0,
            "has_action_verbs": False,
            "has_i": False,
            "score": 0,
            "feedback": ["You didn't type an answer. Try giving at least a short response."],
        }

    words = stripped.split()
    word_count = len(words)
    lower_answer = stripped.lower()

    # Very rough filler count
    filler_count = 0
    for phrase in FILLER_PHRASES:
        # count occurrences of each phrase
        filler_count += lower_answer.count(phrase)

    has_i = " i " in f" {stripped} " or stripped.lower().startswith("i ")
    has_action_verbs = any(verb in lower_answer for verb in ACTION_VERBS)

    # Start from a base score and adjust
    score = 50

    # Length: encourage ~40–120 words
    if word_count < 30:
        feedback.append("Try adding more detail (aim for 40–120 words).")
        score -= 10
    elif word_count > 150:
        feedback.append("Your answer might be too long. Try to be more concise.")
        score -= 5
    else:
        feedback.append("Good length — not too short, not too long.")
        score += 10

    # Action verbs show impact
    if has_action_verbs:
        feedback.append("Nice use of action verbs (designed, built, implemented, etc.).")
        score += 15
    else:
        feedback.append("Try adding action verbs like 'designed', 'implemented', or 'debugged' to show impact.")
        score -= 5

    # Using "I" is good for ownership
    if has_i:
        feedback.append("Good - you use 'I' and take ownership of what you did.")
        score += 5
    else:
        feedback.append("Consider using 'I' to clearly state what *you* did in the situation.")
        score -= 5

    # Penalize filler words
    if filler_count > 0:
        feedback.append("Try to avoid filler words like 'um', 'uh', or 'like'.")
        score -= min(10, filler_count * 2)
    else:
        feedback.append("Nice — no obvious filler words detected.")
        score += 5

    # Clamp score between 0 and 100
    score = max(0, min(100, score))

    return {
        "word_count": word_count,
        "filler_count": filler_count,
        "has_action_verbs": has_action_verbs,
        "has_i": has_i,
        "score": score,
        "feedback": feedback,
    }
