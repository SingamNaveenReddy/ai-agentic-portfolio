# Multi-Agent Task Planner

## Objective

Model a simple multi-agent workflow with separate planning, execution, and review roles.

## How It Works

1. Planner creates steps from a goal.
2. Worker converts steps into actions.
3. Reviewer checks whether the plan is complete.
4. The workflow returns a final status with review notes.

## Run

```bash
python projects/multi-agent-task-planner/run.py
```

## Main File

`ai_projects/task_planner.py`
