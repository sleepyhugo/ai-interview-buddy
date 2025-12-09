from interview.questions import get_random_question
from interview.storage import save_answer, load_recent_answers
from interview.evaluator import evaluate_answer

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def practice_one_question(role: str) -> None:
    # Ask one question, collect answer, evaluate, and show feedback.
    question = get_random_question(role)

    console.print("\n[bold]Question:[/]")
    console.print(f"[italic]{question}[/]\n")

    console.print("When you're ready, type your answer below.\n")
    answer = console.input("> ")

    if answer.lower() == "q":
        console.print("[dim]Cancelled.[/dim]\n")
        return

    # Save the raw answer
    save_answer(role, question, answer)

    # Evaluate the answer
    evaluation = evaluate_answer(answer)

    console.print("\n[bold green]Thanks! Here's your feedback:[/bold green]\n")

    # Summary table
    summary_table = Table(show_header=False, box=None)
    summary_table.add_row("Score", f"{evaluation['score']} / 100")
    summary_table.add_row("Word count", str(evaluation["word_count"]))
    summary_table.add_row("Filler phrases", str(evaluation["filler_count"]))
    summary_table.add_row("Action verbs used", "Yes" if evaluation["has_action_verbs"] else "No")
    summary_table.add_row("Shows ownership ('I')", "Yes" if evaluation["has_i"] else "No")

    console.print(Panel(summary_table, title="Answer Summary", expand=False))

    console.print("\n[bold]Suggestions:[/]")
    for item in evaluation["feedback"]:
        console.print(f"- {item}")

    console.print("\n[dim]Your answer has been saved. You can review it later from the main menu.[/dim]\n")


def show_recent_answers() -> None:
    # Display recent answers from history.
    answers = load_recent_answers(limit=5)

    if not answers:
        console.print("\n[yellow]No past answers found yet. Try practicing a question first![/yellow]\n")
        return

    console.print("\n[bold cyan]Recent Answers[/bold cyan]\n")

    for entry in answers:
        timestamp = entry.get("timestamp", "Unknown time")
        role = entry.get("role", "Unknown role")
        question = entry.get("question", "")
        answer = entry.get("answer", "")

        body = (
            f"[bold]Role:[/] {role}\n"
            f"[bold]Question:[/] {question}\n\n"
            f"[bold]Your answer:[/]\n{answer}"
        )

        console.print(Panel(body, title=timestamp, expand=False))
        console.print()  # blank line between entries


def main():
    console.print(Panel.fit("🤖 AI Interview Buddy", style="bold cyan"))
    console.print("Practice answering interview questions and get instant feedback.\n", style="dim")

    # ask for a role once at the beginning
    role = console.input("[bold]What role are you practicing for (e.g., 'Software Engineer', 'Help Desk')? [/]")
    if role.lower() == "q":
        return

    while True:
        console.print(Panel.fit(
            "[bold]Main Menu[/bold]\n\n"
            "1. Practice a question\n"
            "2. Review recent answers\n"
            "3. Change role\n"
            "q. Quit",
            style="magenta"
        ))

        choice = console.input("Choose an option: ").strip().lower()

        if choice == "1":
            practice_one_question(role)
        elif choice == "2":
            show_recent_answers()
        elif choice == "3":
            role = console.input("\n[bold]Enter a new role:[/] ")
            if role.lower() == "q":
                console.print("[dim]Keeping previous role.[/dim]\n")
        elif choice == "q":
            console.print("\n[bold]Good luck with your interviews! [/bold]\n")
            break
        else:
            console.print("[red]Invalid choice. Please select 1, 2, 3, or q.[/red]\n")


if __name__ == "__main__":
    main()
