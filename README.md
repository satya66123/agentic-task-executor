# 🤖 Agentic Task Executor (From Scratch)

An **Agentic AI system** that takes a high-level task, decomposes it into steps using an LLM, executes steps iteratively using tools, maintains internal memory, and returns a complete execution trace.

✅ Built from scratch in Python (no LangChain / CrewAI)  
✅ Designed to demonstrate real agentic reasoning & orchestration  
✅ Interview-ready project

---

## 🎯 Project Goal

Build an agent that can:

1. Take a high-level task
2. Break it into ordered steps (planning)
3. Execute steps one by one (execution)
4. Maintain simple memory / state (memory)
5. Produce a final structured output (trace)

---

## 🧠 What This Demonstrates

- Task decomposition (planning with LLM)
- Tool execution (tool usage)
- State management (memory)
- Iterative execution loop (agent orchestration)
- Agent traceability (logs)

> This project shows core patterns behind AutoGPT/CrewAI, implemented with minimal readable code.

---

## 📁 Project Structure

agentic-task-executor/
├── agent/
│ ├── init.py
│ ├── planner.py # Task planning using LLM
│ ├── executor.py # Executes a single step using tools
│ ├── memory.py # Stores steps/results/logs
│ └── agent.py # Agent orchestrator loop
├── tools/
│ ├── init.py
│ └── basic_tools.py # Simple tools (write, summarize, research)
├── main.py # Entry point
├── requirements.txt
├── .env
└── README.md



---

## 🔧 Dependencies

openai
python-dotenv
pydantic



---

## 🔐 Environment Setup

Create a `.env` file:

OPENAI_API_KEY=your_openai_api_key_here



⚠️ Do not commit `.env` to GitHub.

---

## ▶️ Run

```bash
python main.py
✅ Progress Timeline
✅ Day 1 — Basic Agent (Completed)
Implemented Components
Memory: stores executed steps + results

Planner: breaks tasks into ordered steps using OpenAI LLM

Executor: executes steps using basic tools + fallback logic

Agent Orchestrator: connects planning → execution → memory

Output (Day 1)
Structured output:

json
Copy code
{
  "steps": ["..."],
  "results": ["..."]
}
✅ Day 2 — Execution Logs + Retry Loop + Smarter Execution (Completed)
Day 2 upgraded the system into a more realistic agent with:

✅ Enhancements Added
Execution logs (traceability)
Each step and result is logged with timestamp.

Retry mechanism + safety controls

max_steps limit

max_retries for robust execution

error logging for debugging

Smarter executor
Executor supports more natural steps:

research steps → research()

write/draft/define/explain → write_text()

summarize → summarize()

Output (Day 2)
Now includes steps + results + logs:

json

{
  "steps": ["..."],
  "results": ["..."],
  "logs": [
    {
      "time": "YYYY-MM-DD HH:MM:SS",
      "message": "STEP ADDED: ..."
    }
  ]
}
🚫 Scope Rules (Intentional)
❌ No vector DB / embeddings / RAG

❌ No UI

❌ No external frameworks (LangChain, CrewAI, AutoGPT)

✅ Pure agent logic with readable code

🧠 Interview Pitch
“I built an agentic AI system from scratch that decomposes tasks using an LLM, executes them step-by-step using tools, maintains execution memory, and logs the full execution trace — without relying on agent frameworks.”

🚀 Next Steps (Day 3 Plan)
Planned improvements:

LLM-based tool selection (dynamic tool routing)

Completion evaluation (done / not done)

Replanning if a plan is weak or incomplete

More memory-aware execution

✅ Day 2 complete. Agent now supports retries, logs, and smarter step execution.



---

## ✅ Day 2 Commit Message (recommended)

After updating README:

git add README.md
git commit -m "Update README with Day 2 progress"
git push
