from datetime import datetime


class AgentMemory:
    def __init__(self):
        self.steps = []
        self.results = []
        self.logs = []

    def add_step(self, step: str):
        self.steps.append(step)
        self.log(f"STEP ADDED: {step}")

    def add_result(self, result: str):
        self.results.append(result)
        self.log(f"RESULT ADDED: {result}")

    def log(self, message: str):
        self.logs.append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "message": message
            }
        )

    def context_text(self) -> str:
        """Short context string for LLM reasoning"""
        context = []
        for i, (s, r) in enumerate(zip(self.steps, self.results), start=1):
            context.append(f"{i}. STEP: {s}\n   RESULT: {r}")
        return "\n".join(context)

    def summary(self):
        return {
            "steps": self.steps,
            "results": self.results,
            "logs": self.logs,
        }
