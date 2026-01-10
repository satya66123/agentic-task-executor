import json
from agent.agent import TaskAgent

if __name__ == "__main__":
    agent = TaskAgent(max_steps=10, max_retries=2)

    output = agent.run(
        "Write a short introduction about LLMs and summarize it"
    )

    print("\nFINAL OUTPUT:\n")
    print(json.dumps(output, indent=2))
