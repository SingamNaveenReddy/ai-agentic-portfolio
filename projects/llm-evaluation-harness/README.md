# LLM Evaluation Harness

## Objective

Create a repeatable evaluation script for checking AI-style outputs.

## How It Works

1. Run fixed questions.
2. Generate answers with the local RAG assistant.
3. Check citations and required concepts.
4. Return pass/fail results in JSON.

## Run

```bash
python projects/llm-evaluation-harness/run.py
```

## Main File

`ai_projects/eval_harness.py`
