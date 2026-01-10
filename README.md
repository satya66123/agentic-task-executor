# 🤖 Agentic Task Executor

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black.svg)
![Stars](https://img.shields.io/github/stars/satya66123/agentic-task-executor?style=social)
![Last Commit](https://img.shields.io/github/last-commit/satya66123/agentic-task-executor)

A lightweight **Agentic AI Task Executor** built from scratch in Python.  
It decomposes a high-level task into ordered steps using an LLM, executes each step iteratively using tools, maintains agent memory, and produces a complete execution trace.

✅ No LangChain / CrewAI / AutoGPT frameworks  
✅ Minimal & readable architecture  
✅ Interview-ready agent design  

---

## 📌 Overview

This project demonstrates the fundamental building blocks of agentic systems:

- **Planning** (task → steps)
- **Execution** (step-by-step tool usage)
- **Memory** (store steps/results/logs)
- **Traceability** (observable JSON output)

---

## ✨ Features

- **LLM-based Task Planning**
  - Converts a high-level goal into structured, ordered steps.

- **Tool-based Execution**
  - Executes steps using a small tool layer:
    - `research`
    - `write_text`
    - `summarize`

- **Agent Memory + Logs**
  - Stores step history, results, and timestamped logs.

- **Structured Output**
  - Returns a complete execution trace in JSON.

- **Fast Demo-Friendly Design**
  - Optimized for stable and quick demos.

---

## 🧠 System Architecture

**Task → Planner → Steps → Executor → Tools → Memory → Final Output**

- `planner.py`: LLM generates steps
- `executor.py`: selects and runs tool for each step
- `memory.py`: records steps/results/logs
- `agent.py`: orchestrates the loop

---

## 📁 Project Structure

agentic-task-executor/
├── agent/
│ ├── planner.py # task → steps (LLM planning)
│ ├── executor.py # step execution + tool routing
│ ├── memory.py # state: steps/results/logs
│ ├── agent.py # orchestration loop
│ ├── tool_selector.py # tool selection logic
│ ├── evaluator.py # completion logic
│ └── replanner.py # optional replanning logic
├── tools/
│ └── basic_tools.py # tool implementations
├── assets/
│ └── demo-output.png
├── main.py
├── requirements.txt
├── .env
├── planner.txt
├── LICENSE.txt
└── README.md



---

## ✅ Quick Start

### 1) Clone the repository

git clone https://github.com/satya66123/agentic-task-executor.git
cd agentic-task-executor
2) Create a virtual environment (recommended)

python -m venv venv
Activate:

Windows (PowerShell):
venv\Scripts\activate
Mac/Linux:

source venv/bin/activate
3) Install dependencies

pip install -r requirements.txt
🔐 Configuration
Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here
⚠️ Never commit .env to GitHub.

▶️ Run
bash
Copy code
python main.py
📤 Example Output (Structure)
json
Copy code
{
  "steps": [
    "Research LLMs and their capabilities",
    "Draft a short introduction",
    "Summarize the introduction"
  ],
  "results": [
    "[research] ...",
    "[write_text] ...",
    "[summarize] ..."
  ],
  "logs": [
    {
      "time": "YYYY-MM-DD HH:MM:SS",
      "message": "STEP ADDED: ..."
    }
  ]
}
📸 Demo Output Screenshot
A sample run demonstrating planning, execution and logging:


🛣️ Roadmap (Optional Enhancements)
Add .env switch for fast vs autonomous execution mode

JSON schema-based structured plans

Unit tests for tools and memory

More tools (file writer, web search, calculator)

Docker support

👤 Author
Satya Srinath
GitHub: https://github.com/satya66123
Email: satyasrinath653512@gmail.com

📜 License
This project is licensed under the MIT License.
See LICENSE.txt for more information.


git commit -m "Improve README with professional documentation"
git push
