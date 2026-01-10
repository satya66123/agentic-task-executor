from tools.basic_tools import TOOLS
from agent.tool_selector import select_tool


def execute_step(step: str, memory_context: str = ""):
    tool_name = select_tool(step, memory_context)
    tool_fn = TOOLS[tool_name]

    return tool_name, tool_fn(step)
