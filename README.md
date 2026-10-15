This is an AI agent which acts as a research assistant.

This is for demo purposes only - on how to build a simple AI agent.

What is an AI agent?

An AI agent is a more autonomous system. It doesn’t just retrieve info, it reasons about a goal, breaks it down into steps, and uses tools to complete them.

If we split AI into three levels:

1. Input --> LLM --> Output (Answers)
2. Input --> RAG --> Output (Reads)
3. Input --> Action --> Output (Acts/Thinks)

It can decide to use some of it's provided tools to:

- Search Wikipedia
- Search DuckDuckGo
- Search a CSV
- Save the output to a text file

Topics:

- Validation (correct output format)
- Tools (what can the agent actually do)
- Control (logic to handle a query)

Files:

* agent.py - fully autonomous decides which tools to use so more risk
* control.py - semi-autonomous predicts intent and we route to tools so more control over business logic

Resources:

- https://github.com/daveebbelaar/ai-cookbook/tree/main/agents/building-blocks