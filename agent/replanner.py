import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def replan(task: str, memory_context: str) -> list[str]:
    prompt = f"""
You are a replanning agent.

Task:
{task}

Execution so far:
{memory_context}

The current plan is not good enough.
Generate a better remaining step plan (only remaining steps).
Return only numbered steps list.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    steps_text = response.choices[0].message.content

    steps = [s.strip() for s in steps_text.split("\n") if s.strip()]
    return steps
