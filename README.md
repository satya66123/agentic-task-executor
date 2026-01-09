# agentic-task-executor
🤖 Agentic Task Executor – Day 1

An agentic AI system that takes a high-level task, breaks it into steps, executes them sequentially, maintains internal memory, and returns a complete execution trace.

Built from scratch without agent frameworks.

🎯 Goal (Day 1)

Build a minimal agent that demonstrates:

Task decomposition (planning)

Step-by-step execution

Tool usage

In-memory state tracking

End-to-end agent loop

🧠 What This Demonstrates

Agentic reasoning

LLM-based planning

Deterministic execution flow

Memory and state handling

Clean separation of responsibilities

No LangChain, no CrewAI — pure Python logic.

📁 Project Structure
agentic-task-executor/
├── agent/
│   ├── planner.py    # Task decomposition using LLM
│   ├── executor.py   # Executes individual steps
│   ├── memory.py     # Stores steps and results
│   └── agent.py      # Orchestrates the agent loop
├── tools/
│   └── basic_tools.py
├── main.py           # Entry point
├── requirements.txt
├── .env
└── README.md

🔧 Dependencies
openai
python-dotenv
pydantic

🔐 Environment Setup

Create a .env file:

OPENAI_API_KEY=your_openai_api_key

▶️ How It Works

Planner breaks a high-level task into ordered steps using an LLM

Executor runs each step using simple tools or default execution

Memory stores all steps and results

Agent orchestrates planning → execution → memory

▶️ Run the Agent
python main.py

✅ Sample Output
{
  "steps": [
    "1. Define what LLMs are",
    "2. Explain how LLMs work",
    "3. Summarize the introduction"
  ],
  "results": [
    "Executed step successfully...",
    "Executed step successfully...",
    "Summarize the introduction..."
  ]
}

