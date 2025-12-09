from interview.evaluator import evaluate_answer


def test_evaluate_answer_returns_expected_keys():
    result = evaluate_answer("I designed and implemented a small tool to automate reports.")
    # basic keys
    assert "word_count" in result
    assert "filler_count" in result
    assert "has_action_verbs" in result
    assert "has_i" in result
    assert "score" in result
    assert "feedback" in result

    assert isinstance(result["word_count"], int)
    assert isinstance(result["score"], int)
    assert isinstance(result["feedback"], list)
