# Local RAG Assistant

## Objective

Build a local question-answering assistant that retrieves information from Markdown documents and returns citations.

## How It Works

1. Load documents from `data/knowledge_base`.
2. Split documents into sentence chunks.
3. Score chunks based on the question.
4. Generate an answer from the highest scoring evidence.
5. Return the source files used.

## Run

```bash
python projects/local-rag-assistant/run.py
```

## Main File

`ai_projects/rag_assistant.py`
