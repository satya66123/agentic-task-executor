import json
from agent.agent import TaskAgent

if __name__ == "__main__":
    print("✅ Starting agent...")

    agent = TaskAgent(max_steps=4, max_retries=0)

    task = "Write a 3-line introduction about LLMs and summarize it in 1 line"


    print("✅ Running task:", task)
    output = agent.run(task)

    print("✅ FINAL OUTPUT:")
    print(json.dumps(output, indent=2))
