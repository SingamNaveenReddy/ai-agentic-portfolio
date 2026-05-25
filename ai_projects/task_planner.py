from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanResult:
    goal: str
    steps: list[str]
    actions: list[str]
    review_notes: list[str]
    status: str


class PlannerAgent:
    def create_steps(self, goal: str) -> list[str]:
        return [
            f"Define the expected output for: {goal}",
            "Identify the information or tools required.",
            "Break the work into small executable actions.",
            "Review the final result for missing pieces.",
        ]


class WorkerAgent:
    def create_actions(self, steps: list[str]) -> list[str]:
        return [
            f"Action {index}: {step}"
            for index, step in enumerate(steps, start=1)
        ]


class ReviewerAgent:
    def review(self, goal: str, actions: list[str]) -> tuple[str, list[str]]:
        notes: list[str] = []
        if not goal.strip():
            notes.append("Goal is empty.")
        if len(actions) < 3:
            notes.append("Plan needs more execution detail.")
        if not any("Review" in action for action in actions):
            notes.append("Plan should include a review step.")

        if notes:
            return "needs_revision", notes
        return "ready", ["Plan includes goal, execution steps, and review."]


class MultiAgentTaskPlanner:
    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.worker = WorkerAgent()
        self.reviewer = ReviewerAgent()

    def run(self, goal: str) -> PlanResult:
        steps = self.planner.create_steps(goal)
        actions = self.worker.create_actions(steps)
        status, notes = self.reviewer.review(goal, actions)
        return PlanResult(
            goal=goal,
            steps=steps,
            actions=actions,
            review_notes=notes,
            status=status,
        )


def main() -> None:
    result = MultiAgentTaskPlanner().run("Prepare a reliable RAG evaluation workflow")
    print(f"Goal: {result.goal}")
    print(f"Status: {result.status}")
    print("\nActions:")
    for action in result.actions:
        print(f"- {action}")
    print("\nReview:")
    for note in result.review_notes:
        print(f"- {note}")


if __name__ == "__main__":
    main()
