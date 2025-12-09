from interview.questions import get_random_question
from interview.storage import save_answer
from interview.evaluator import evaluate_answer

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def main():
    console.print(Panel.fit("AI Interview Buddy", style="bold cyan"))
    console.print("Practice answering interview questions and get instant feedback.\n", style="dim")

    console.print("Type 'q' at any time to quit.\n", style="yellow")

    role = console.input("[bold]What role are you practicing for (e.g., 'Software Engineer', 'Help Desk')? [/]")
    if role.lower() == "q":
        return

    question = get_random_question(role)
    console.print("\n[bold]Question:[/]")
    console.print(f"[italic]{question}[/]\n")

    console.print("When you're ready, type your answer below.\n")
    answer = console.input("> ")

    if answer.lower() == "q":
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

    console.print("\n[dim]Your answer has been saved. You can review it later in the data/ folder.[/dim]\n")


if __name__ == "__main__":
    main()
