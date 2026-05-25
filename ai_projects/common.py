from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE = ROOT / "data" / "knowledge_base"
TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_+-]*")


@dataclass(frozen=True)
class Document:
    source: str
    title: str
    text: str


@dataclass(frozen=True)
class Chunk:
    source: str
    title: str
    text: str
    score: float = 0.0


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_RE.finditer(text)]


def load_documents(path: Path = KNOWLEDGE_BASE) -> list[Document]:
    documents: list[Document] = []
    for file_path in sorted(path.glob("*.md")):
        text = file_path.read_text(encoding="utf-8").strip()
        title = text.splitlines()[0].lstrip("# ").strip()
        documents.append(Document(source=file_path.name, title=title, text=text))
    return documents


def chunk_document(document: Document, max_sentences: int = 3) -> list[Chunk]:
    body = "\n".join(
        line for line in document.text.splitlines() if not line.startswith("#")
    ).strip()
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", body.replace("\n", " "))
        if sentence.strip()
    ]
    chunks: list[Chunk] = []
    for index in range(0, len(sentences), max_sentences):
        chunk_text = " ".join(sentences[index : index + max_sentences])
        chunks.append(Chunk(source=document.source, title=document.title, text=chunk_text))
    return chunks


def score_text(query: str, text: str) -> float:
    query_terms = set(tokenize(query))
    text_terms = tokenize(text)
    if not query_terms or not text_terms:
        return 0.0
    overlap = sum(1 for term in text_terms if term in query_terms)
    density = overlap / max(len(text_terms), 1)
    coverage = len(query_terms.intersection(text_terms)) / len(query_terms)
    return round(coverage * 0.75 + density * 0.25, 4)
