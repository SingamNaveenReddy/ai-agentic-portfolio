from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ai_projects.rag_assistant import answer_question


if __name__ == "__main__":
    result = answer_question("How should I evaluate a RAG system?")
    print(result["answer"])
    print("Citations:", ", ".join(result["citations"]) or "none")
