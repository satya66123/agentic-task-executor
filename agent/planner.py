import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionUserMessageParam,
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def plan_task(task: str) -> list[str]:
    prompt = f"""
Break the following task into clear, ordered steps.

Task: {task}

Return only a numbered list.
"""

    messages: list[ChatCompletionUserMessageParam] = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    steps_text = response.choices[0].message.content

    steps = [
        step.strip()
        for step in steps_text.split("\n")
        if step.strip()
    ]

    return steps
