def show_history() -> None:
    print("\n== Brief History of Python ==")
    print(" - Created in 1991")
    print(" - Python 3 released in 2008")
    print("\nProgram that computes average score of students\n")


def get_names_scores() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores:")

    for i in range(count):
        name = input(f"Student {i + 1} name: ").strip()
        if not name:
            name = f"Student{i+1}"
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return names_of_students, scores


def compute_average(scores: list[float]) -> float:
    if scores:
        return sum(scores) / len(scores)
    return 0.0


def main():
    show_history()
    names, scores = get_names_scores()
    avg_score = compute_average(scores)

    print("\n== Student Scores ==")
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

    print(f"\nAverage Score: {avg_score:.2f}")


if __name__ == "__main__":
    main()
