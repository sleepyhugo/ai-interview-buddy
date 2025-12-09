def evaluate_answer(answer: str) -> dict:
    # Very simple placeholder evaluation.
    word_count = len(answer.split())

    feedback = []
    if word_count < 30:
        feedback.append("Try giving a bit more detail.")
    else:
        feedback.append("Nice length. Now make sure it's focused and clear.")

    return {
        "word_count": word_count,
        "feedback": feedback,
    }
