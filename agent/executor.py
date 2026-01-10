from tools.basic_tools import write_text, summarize, research


def execute_step(step: str):
    step_lower = step.lower()

    if "research" in step_lower:
        return research(step)

    if "write" in step_lower or "draft" in step_lower or "define" in step_lower or "explain" in step_lower:
        return write_text(step)

    if "summarize" in step_lower:
        return summarize(step)

    return f"Executed step successfully: {step}"
