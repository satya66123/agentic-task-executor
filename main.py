from agent.agent import TaskAgent

if __name__ == "__main__":
    agent = TaskAgent()

    output = agent.run(
        "Write a short introduction about LLMs and summarize it"
    )

    print("FINAL OUTPUT:")
    print(output)
