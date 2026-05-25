# Interview Guide

Use this as a quick way to explain the repository in interviews.

## Short Pitch

This repo is a local-first AI engineering portfolio. It shows how I would structure agentic systems before connecting expensive model APIs: retrieval, state, evidence, evaluation, tests, and CI are all visible in simple Python code.

## Project Talking Points

### Research Brief Agent

- Demonstrates planner-executor-reviewer style agent design.
- Keeps state explicit with `AgentState`.
- Produces a cited brief instead of an unsupported answer.
- Includes a self-check step so the agent can flag missing citations or missing recommendations.

### Local RAG Assistant

- Loads Markdown documents from a small knowledge base.
- Chunks documents into sentence groups.
- Scores chunks with transparent lexical retrieval.
- Returns an answer with citations and a fallback when evidence is missing.

### Evaluation Harness

- Treats AI outputs like software behavior that can regress.
- Runs fixed test questions.
- Checks citation count, required concept coverage, and pass/fail status.
- Produces JSON output that can be used in CI.

## Tradeoffs

- I used standard-library Python to make the system easy to review without API keys.
- The retrieval scorer is simple by design; a production version could replace it with embeddings and reranking.
- The evaluation harness is deterministic, which is useful for CI, but a production evaluator could add model-graded rubric checks.

## How I Would Improve It Next

- Add a Streamlit UI for interactive demos.
- Add OpenAI or local LLM adapters behind the same interfaces.
- Add persistent run logs for agent traces.
- Expand the evaluation dataset and track prompt versions.
