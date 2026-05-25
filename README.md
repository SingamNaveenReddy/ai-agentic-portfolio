# AI Agentic Projects

A collection of small AI engineering projects focused on agents, retrieval, evaluation, and multi-step workflows. Each project is kept in its own folder with a short report, runnable code, and tests.

## Projects

| Folder | Project | Focus |
| --- | --- | --- |
| `projects/research-brief-agent` | Research Brief Agent | Planning, retrieval, cited report generation, self-checking |
| `projects/local-rag-assistant` | Local RAG Assistant | Chunking, retrieval, citation-aware question answering |
| `projects/llm-evaluation-harness` | LLM Evaluation Harness | Deterministic checks for groundedness and required concept coverage |
| `projects/multi-agent-task-planner` | Multi-Agent Task Planner | Planner, worker, and reviewer style task coordination |

The examples use local Markdown data and standard-library Python so they can run without API keys.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
```

## Run Examples

```bash
python projects/research-brief-agent/run.py
python projects/local-rag-assistant/run.py
python projects/llm-evaluation-harness/run.py
python projects/multi-agent-task-planner/run.py
```

The same modules can also be run directly:

```bash
python -m ai_projects.research_agent
python -m ai_projects.rag_assistant --question "How should I evaluate a RAG system?"
python -m ai_projects.eval_harness
python -m ai_projects.task_planner
```

## Structure

```text
projects/
  research-brief-agent/
  local-rag-assistant/
  llm-evaluation-harness/
  multi-agent-task-planner/
ai_projects/
  common.py
  research_agent.py
  rag_assistant.py
  eval_harness.py
  task_planner.py
data/
  knowledge_base/
docs/
  PROJECT_REPORT.md
tests/
```

## Notes

- The code is intentionally simple and readable.
- The projects use deterministic local logic first.
- External LLM APIs can be added later behind the same project interfaces.
- Tests and CI are included so changes can be checked automatically.
