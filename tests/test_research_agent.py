from agentic_portfolio.research_agent import ResearchBriefAgent


def test_research_agent_writes_cited_brief():
    brief, state = ResearchBriefAgent().run("What makes agent workflows reliable?")

    assert "# Research Brief" in brief
    assert "Sources" in brief
    assert state.citations
    assert state.self_check == ["All claims are tied to retrieved local evidence."]
