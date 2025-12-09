from interview.evaluator import evaluate_answer


def test_evaluate_answer_returns_word_count():
    result = evaluate_answer("This is a short test answer.")
    assert "word_count" in result
    assert isinstance(result["word_count"], int)
