from agent.planner import plan_task
from agent.executor import execute_step
from agent.memory import AgentMemory


class TaskAgent:
    def __init__(self):
        self.memory = AgentMemory()

    def run(self, task: str):
        steps = plan_task(task)

        if not steps:
            steps = ["Write content", "Summarize content"]

        for step in steps:
            self.memory.add_step(step)
            result = execute_step(step)
            self.memory.add_result(result)

        return self.memory.summary()
