from agent.planner import plan_task
from agent.executor import execute_step
from agent.memory import AgentMemory


class TaskAgent:
    def __init__(self, max_steps: int = 10, max_retries: int = 2):
        self.memory = AgentMemory()
        self.max_steps = max_steps
        self.max_retries = max_retries

    def run(self, task: str):
        steps = plan_task(task)

        if not steps:
            steps = ["Write content", "Summarize content"]

        executed = 0

        for step in steps:
            if executed >= self.max_steps:
                self.memory.log("STOPPED: max_steps limit reached")
                break

            self.memory.add_step(step)

            retries = 0
            while retries <= self.max_retries:
                try:
                    result = execute_step(step)
                    self.memory.add_result(result)
                    break
                except Exception as e:
                    retries += 1
                    self.memory.log(f"ERROR on step: {step} | retry {retries} | {str(e)}")

                    if retries > self.max_retries:
                        self.memory.add_result(f"FAILED step after retries: {step}")

            executed += 1

        return self.memory.summary()
