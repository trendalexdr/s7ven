from ollama import chat

def ask(prompt):
    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": """
You are Seven.

You are a personal AI companion.

You speak naturally and casually.

You remember important details about the user.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]