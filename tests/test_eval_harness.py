from agentic_portfolio.eval_harness import run_evaluation


def test_evaluation_harness_passes_baseline_cases():
    result = run_evaluation()

    assert result["passed"] is True
    assert len(result["cases"]) == 2
