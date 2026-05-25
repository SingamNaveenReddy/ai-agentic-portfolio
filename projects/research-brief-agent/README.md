# Research Brief Agent

## Objective

Create an agent that answers a question by planning the work, retrieving local evidence, writing a brief, and checking the result.

## How It Works

1. The agent creates a short task plan.
2. It retrieves relevant chunks from the local knowledge base.
3. It writes a research brief with findings and citations.
4. It checks whether the brief includes citations and a recommendation.

## Run

```bash
python projects/research-brief-agent/run.py
```

## Main File

`ai_projects/research_agent.py`
