from ai_projects.rag_assistant import answer_question, retrieve


def test_retrieve_returns_ranked_chunks_for_relevant_question():
    chunks = retrieve("How do I evaluate RAG with citations?")

    assert chunks
    assert chunks[0].score > 0
    assert chunks[0].source == "rag_evaluation.md"


def test_answer_includes_citations():
    result = answer_question("What makes an AI project strong?")

    assert result["citations"]
    assert "local knowledge base" in result["answer"]
