from agent.planner import plan_task
from agent.executor import execute_step
from agent.evaluator import evaluate_step
from agent.memory import AgentMemory


class TaskAgent:
    def __init__(self, max_steps: int = 12, max_retries: int = 0):
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
            done = False

            while retries <= self.max_retries and not done:
                memory_context = self.memory.context_text()
                tool_used, result = execute_step(step, memory_context)
                self.memory.add_result(f"[{tool_used}] {result}")

                done = evaluate_step(step, result)

                if not done:
                    retries += 1
                    self.memory.log(f"NOT DONE: retrying step ({retries}) -> {step}")

                    if retries > self.max_retries:
                        self.memory.add_result(f"FAILED step after retries: {step}")
                        break

            executed += 1

        return self.memory.summary()