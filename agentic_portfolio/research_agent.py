from __future__ import annotations

from dataclasses import dataclass, field

from .rag_assistant import retrieve


@dataclass
class AgentState:
    question: str
    plan: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    citations: list[str] = field(default_factory=list)
    self_check: list[str] = field(default_factory=list)


class ResearchBriefAgent:
    def plan(self, state: AgentState) -> AgentState:
        state.plan = [
            "Clarify the decision the reader needs to make.",
            "Retrieve evidence from the local knowledge base.",
            "Write a brief answer with source citations.",
            "Check whether claims are supported by evidence.",
        ]
        return state

    def gather_evidence(self, state: AgentState) -> AgentState:
        chunks = [chunk for chunk in retrieve(state.question, limit=5) if chunk.score > 0]
        state.evidence = [chunk.text for chunk in chunks]
        state.citations = sorted({chunk.source for chunk in chunks})
        return state

    def write_brief(self, state: AgentState) -> str:
        if not state.evidence:
            return "No supported brief could be created from the local knowledge base."

        top_points = "\n".join(f"- {text}" for text in state.evidence[:3])
        citations = ", ".join(state.citations)
        return (
            f"# Research Brief\n\n"
            f"Question: {state.question}\n\n"
            f"## Key Findings\n{top_points}\n\n"
            f"## Recommendation\n"
            f"Start with a narrow, measurable agent workflow and add evaluation before adding more tools.\n\n"
            f"## Sources\n{citations}"
        )

    def check(self, state: AgentState, brief: str) -> AgentState:
        state.self_check = []
        if "Sources" not in brief or not state.citations:
            state.self_check.append("Brief is missing citations.")
        if "Recommendation" not in brief:
            state.self_check.append("Brief is missing a decision-oriented recommendation.")
        if not state.self_check:
            state.self_check.append("All claims are tied to retrieved local evidence.")
        return state

    def run(self, question: str) -> tuple[str, AgentState]:
        state = self.plan(AgentState(question=question))
        state = self.gather_evidence(state)
        brief = self.write_brief(state)
        state = self.check(state, brief)
        return brief, state


def main() -> None:
    agent = ResearchBriefAgent()
    brief, state = agent.run("What makes an AI agent portfolio strong?")
    print(brief)
    print("\nSelf-check:", "; ".join(state.self_check))


if __name__ == "__main__":
    main()
