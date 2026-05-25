from ai_projects.task_planner import MultiAgentTaskPlanner


def test_multi_agent_task_planner_returns_ready_plan():
    result = MultiAgentTaskPlanner().run("Create a RAG evaluation checklist")

    assert result.status == "ready"
    assert len(result.steps) == 4
    assert len(result.actions) == 4
    assert result.review_notes == ["Plan includes goal, execution steps, and review."]
