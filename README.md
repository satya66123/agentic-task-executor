# 🤖 Agentic Task Executor

An **agentic AI system** built from scratch that can take a high-level task, decompose it into ordered steps, execute each step using tools, maintain memory, and return a complete execution trace.


---

## 🎯 Features

- **Task Planning (LLM-based)**  
  Converts a high-level goal into structured step-by-step plan.

- **Iterative Execution Loop**  
  Executes steps one-by-one in sequence.

- **Tool Routing / Tool Usage**
  Uses built-in tools such as:
  - `research`
  - `write_text`
  - `summarize`

- **Agent Memory**
  Stores:
  - executed steps
  - results
  - execution logs (timestamps)

- **Traceable Output**
  Returns full structured JSON for transparency and debugging.

---

## 🧠 How It Works

1. **Planner** generates steps from the task (LLM)
2. **Executor** selects and executes the correct tool for each step
3. **Memory** stores steps + results and logs
4. **Agent** orchestrates the full loop and returns final output

---

## 📁 Project Structure

agentic-task-executor/
├── agent/
│ ├── planner.py
│ ├── executor.py
│ ├── memory.py
│ ├── agent.py
│ ├── tool_selector.py
│ ├── evaluator.py
│ └── replanner.py
├── tools/
│ └── basic_tools.py
├── main.py
├── requirements.txt
├── .env
├── LICENSE.txt
└── README.md



---

## 🔧 Requirements

- Python 3.10+
- OpenAI API Key

Install dependencies:

```bash
pip install -r requirements.txt
🔐 Environment Setup
Create .env file:

txt
Copy code
OPENAI_API_KEY=your_openai_api_key_here
⚠️ Do not commit .env to GitHub.

▶️ Run

python main.py
✅ Example Output (Structure)
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
🧠 Interview Pitch
“I built an agentic AI system from scratch that decomposes tasks using an LLM, executes them step-by-step using tools, maintains memory, and returns the full execution trace — without frameworks.”

📜 License
This project is licensed under the MIT License. See LICENSE.txt.

python


---

## 2) ✅ `agent/planner.py` (clean + separate steps)

👉 Replace your **`agent/planner.py`** with this:

```python
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def _clean_steps(text: str) -> list[str]:
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    steps: list[str] = []

    for line in lines:
        # Remove numbering/bullets like: "1.", "1)", "-", "*"
        cleaned = re.sub(r"^(\d+[\.\)]|\-|\*)\s*", "", line).strip()

        if not cleaned:
            continue

        # Filter out non-step noise
        if cleaned.lower().startswith(("task:", "note:", "explanation:")):
            continue

        steps.append(cleaned)

    return steps


def plan_task(task: str) -> list[str]:
    prompt = f"""
Break the following task into clear, ordered steps.
Each step must be short and actionable.

Task: {task}

Return ONLY a numbered list of steps.
Do not add explanations.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw = response.choices[0].message.content or ""
    steps = _clean_steps(raw)

    # Fallback plan
    if not steps:
        steps = [
            "Research the topic",
            "Write the required content",
            "Summarize the final content"
        ]

    return steps
✅ Now planner returns steps like:

Research the topic

Write the required content

Summarize the final content

3) ✅ MIT License (LICENSE.txt)
Create LICENSE.txt in root folder and paste this:


MIT License

Copyright (c) 2026 Satya Nani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
✅ Final Commit (after changes)

git add .
git commit -m "Finalize README, improve planner step parsing, add MIT license"
git push
