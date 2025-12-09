import random

GENERAL_QUESTIONS = [
    "Tell me about yourself.",
    "Describe a challenging problem you solved.",
    "Tell me about a time you worked in a team.",
]

SWE_QUESTIONS = [
    "Tell me about a time you debugged a difficult issue.",
    "Describe a project you’re proud of.",
    "How do you ensure the quality of your code?",
]


def get_random_question(role: str) -> str:
    # Return a random question based on the role (very simple for now).
    role_lower = role.lower()

    if "engineer" in role_lower or "developer" in role_lower:
        pool = GENERAL_QUESTIONS + SWE_QUESTIONS
    else:
        pool = GENERAL_QUESTIONS

    return random.choice(pool)
