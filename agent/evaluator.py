def evaluate_step(step: str, result: str) -> bool:
    """
    SUPER FAST MODE evaluator (rule-based, no LLM call)
    Always marks step as DONE if result is non-empty.
    """
    return bool(result and result.strip())
