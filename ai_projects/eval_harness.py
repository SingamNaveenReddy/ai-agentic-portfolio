from __future__ import annotations

import json

from .rag_assistant import answer_question


EVAL_CASES = [
    {
        "question": "How should I evaluate a RAG system?",
        "required_terms": {"citations", "grounded", "regression"},
    },
    {
        "question": "What makes agent workflows reliable?",
        "required_terms": {"tools", "state", "evaluation"},
    },
]


def score_case(question: str, required_terms: set[str]) -> dict[str, object]:
    result = answer_question(question)
    answer = str(result["answer"]).lower()
    citations = result["citations"]
    covered_terms = sorted(term for term in required_terms if term in answer)

    return {
        "question": question,
        "citation_count": len(citations),
        "coverage": round(len(covered_terms) / len(required_terms), 2),
        "covered_terms": covered_terms,
        "passed": bool(citations) and len(covered_terms) >= max(1, len(required_terms) - 1),
    }


def run_evaluation() -> dict[str, object]:
    cases = [
        score_case(case["question"], case["required_terms"])
        for case in EVAL_CASES
    ]
    return {
        "passed": all(case["passed"] for case in cases),
        "cases": cases,
    }


def main() -> None:
    print(json.dumps(run_evaluation(), indent=2))


if __name__ == "__main__":
    main()
