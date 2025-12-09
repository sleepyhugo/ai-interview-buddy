from interview.questions import get_random_question
from interview.storage import save_answer


def main():
    print("=== AI Interview Buddy ===")
    print("Type 'q' at any time to quit.\n")

    role = input("What role are you practicing for (e.g., 'Software Engineer', 'Help Desk')? ")
    if role.lower() == "q":
        return

    question = get_random_question(role)
    print("\nQuestion:")
    print(f"> {question}\n")

    answer = input("Your answer:\n> ")
    if answer.lower() == "q":
        return

    # For now just save it (improve this later)
    save_answer(role, question, answer)
    print("\nThanks! Your answer has been saved.")


if __name__ == "__main__":
    main()
