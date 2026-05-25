# AI Agentic Portfolio

Practical AI engineering projects focused on agents, retrieval, evaluation, and data workflows. The goal of this repo is to show how I think about building AI systems that are useful, testable, and explainable.

## What Is Inside

| Project | What it demonstrates | Entry point |
| --- | --- | --- |
| Research Brief Agent | Agent loop with planning, tool use, source grounding, and report writing | `python -m agentic_portfolio.research_agent` |
| Local RAG Assistant | Chunking, retrieval, citation-aware answers, and deterministic fallback behavior | `python -m agentic_portfolio.rag_assistant` |
| LLM Evaluation Harness | Regression-style checks for AI outputs using groundedness, coverage, and format metrics | `python -m agentic_portfolio.eval_harness` |

All examples run locally with the Python standard library. That makes the repo easy to review, test, and extend before connecting external model APIs.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

Run the demos:

```bash
python -m agentic_portfolio.research_agent
python -m agentic_portfolio.rag_assistant --question "How should I evaluate a RAG system?"
python -m agentic_portfolio.eval_harness
```

## Design Notes

### Research Brief Agent

The research agent uses a small planner-executor pattern:

1. Build a task plan from the user question.
2. Search a local knowledge base.
3. Extract relevant evidence.
4. Generate a short brief with citations.
5. Run a self-check for missing evidence.

This mirrors production agent design without hiding the logic behind a black-box framework.

### Local RAG Assistant

The RAG assistant implements document loading, sentence chunking, token scoring, retrieval, and answer synthesis. It favors transparent ranking over complex dependencies so the retrieval behavior is easy to debug.

### Evaluation Harness

The evaluator treats AI behavior like software behavior. It runs fixed cases and reports:

- citation coverage
- answer groundedness
- required concept coverage
- concise JSON output for CI

## Repository Structure

```text
agentic_portfolio/
  common.py
  research_agent.py
  rag_assistant.py
  eval_harness.py
data/
  knowledge_base/*.md
tests/
  test_*.py
.github/workflows/ci.yml
```

## Next Improvements

- Add an OpenAI/LangChain/LlamaIndex adapter while keeping local fallback tests.
- Add a Streamlit or FastAPI UI for the RAG assistant.
- Add prompt/version tracking for evaluation runs.
- Add Docker support for repeatable demos.

## Why This Repo Matters

Hiring managers usually look for more than notebooks. This repo is built to show end-to-end AI engineering habits: clean code, reproducible examples, tests, documentation, and the ability to explain tradeoffs.
