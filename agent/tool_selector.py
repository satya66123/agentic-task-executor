def select_tool(step: str, memory_context: str = "") -> str:
    """
    SUPER FAST MODE tool selection (rule-based, no LLM call)
    """
    s = step.lower()

    if any(word in s for word in ["research", "gather", "collect", "find", "learn"]):
        return "research"

    if any(word in s for word in ["summarize", "summary", "shorten", "brief"]):
        return "summarize"

    if any(word in s for word in ["write", "draft", "introduce", "define", "explain", "conclude"]):
        return "write_text"

    return "write_text"
