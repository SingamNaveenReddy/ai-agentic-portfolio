from __future__ import annotations

import argparse
from dataclasses import replace

from .common import Chunk, chunk_document, load_documents, score_text


def build_index() -> list[Chunk]:
    chunks: list[Chunk] = []
    for document in load_documents():
        chunks.extend(chunk_document(document))
    return chunks


def retrieve(question: str, limit: int = 4) -> list[Chunk]:
    ranked = [
        replace(chunk, score=score_text(question, chunk.text))
        for chunk in build_index()
    ]
    return sorted(ranked, key=lambda chunk: chunk.score, reverse=True)[:limit]


def answer_question(question: str, limit: int = 4) -> dict[str, object]:
    evidence = [chunk for chunk in retrieve(question, limit=limit) if chunk.score > 0]
    if not evidence:
        return {
            "answer": "I do not have enough local evidence to answer that question.",
            "citations": [],
        }

    strongest = evidence[0]
    citations = sorted({chunk.source for chunk in evidence})
    answer = (
        f"Based on the local knowledge base, {strongest.text} "
        f"I would validate this with {len(evidence)} retrieved evidence chunk(s)."
    )
    return {"answer": answer, "citations": citations}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local RAG assistant.")
    parser.add_argument(
        "--question",
        default="How should I evaluate a RAG system?",
        help="Question to ask the local knowledge base.",
    )
    args = parser.parse_args()
    result = answer_question(args.question)
    print(result["answer"])
    print("Citations:", ", ".join(result["citations"]) or "none")


if __name__ == "__main__":
    main()
