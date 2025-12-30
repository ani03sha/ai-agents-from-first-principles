# Day 0:

## Define and "agent" without using the words: AI, intelligence, LLM, model, reasoning, chatbot.
An agent is a system that uses observations about its environment and its internal state to perform actions over time on its own. An agent controls its interaction with the environment over time while a simple function returns an output for an input.

## What is the minimum internal component an agent must have that a non-agent system does not?
The agent should have "policy" as the minimum component. A policy is the only internal component that maps **observation** and **internal state** to produce action. It exists even if it is trivial, fixed, or random. Policy makes the system decisional, not merely reactive.

## Important points
- An agent is a control system over time
- Agent-ness is defined by internal structure, not intelligence
- Policy is the irreducible core
- Learning is not required
- LLMs are implementation details, not the concept
