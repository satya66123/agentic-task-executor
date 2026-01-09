class AgentMemory:
    def __init__(self):
        self.steps = []
        self.results = []

    def add_step(self, step):
        self.steps.append(step)

    def add_result(self, result):
        self.results.append(result)

    def summary(self):
        return {
            "steps": self.steps,
            "results": self.results
        }
