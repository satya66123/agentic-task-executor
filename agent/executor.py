from tools.basic_tools import write_text, summarize


def execute_step(step: str):
    step_lower = step.lower()

    if "write" in step_lower or "draft" in step_lower:
        return write_text(step)

    if "summarize" in step_lower:
        return summarize(step)

    # Default execution for non-tool steps
    return f"Executed step successfully: {step}"
