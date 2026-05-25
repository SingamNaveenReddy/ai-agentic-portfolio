# AI Projects Report

## Overview

This repository contains four AI-focused projects. The projects are designed around common AI application patterns: retrieval, agent state, task planning, evaluation, and evidence-based responses.

## Project 1: Research Brief Agent

### Objective

Create a small agent that can take a question, gather local evidence, and produce a short cited research brief.

### Main Steps

1. Create a plan for the question.
2. Retrieve relevant knowledge-base chunks.
3. Write a short brief using the retrieved evidence.
4. Run a self-check for citations and recommendation quality.

### Output

The project generates a Markdown-style research brief with key findings, a recommendation, and source citations.

## Project 2: Local RAG Assistant

### Objective

Build a local retrieval augmented generation style assistant that answers questions using local documents.

### Main Steps

1. Load Markdown documents.
2. Split each document into sentence chunks.
3. Score chunks against the user question.
4. Generate an answer using the highest ranked evidence.
5. Return source citations.

### Output

The assistant returns an answer and a list of local source files used as citations.

## Project 3: LLM Evaluation Harness

### Objective

Create a small evaluation runner that checks whether AI responses satisfy basic quality requirements.

### Main Checks

- citation count
- required concept coverage
- pass/fail status for each evaluation case
- JSON output for easy automation

### Output

The project returns a structured JSON report with case-level scores.

## Project 4: Multi-Agent Task Planner

### Objective

Model a simple multi-agent workflow where different roles handle planning, execution, and review.

### Main Roles

- Planner: breaks a goal into steps.
- Worker: converts steps into actions.
- Reviewer: checks whether the actions are complete and practical.

### Output

The project returns a task plan, action list, review notes, and final status.

## Common Design Choices

- Local data is used first so examples are reproducible.
- The code avoids hidden framework behavior.
- Each project has a focused scope.
- Tests cover the main behavior of the projects.

## Future Work

- Add a small web interface for the RAG assistant.
- Add OpenAI or local model adapters.
- Add persistent trace logs for agent runs.
- Expand the evaluation cases with more questions.
