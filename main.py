import random

# Random module is used to select random words from the list
words = ["apple", "banana", "cherry", "mango", "litchi", "orange", "grape"]

# ASCII art for the hangman representation
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" 0 ", "   ", "   "),
    2: (" 0 ", " | ", "   "),
    3: (" 0 ", "/| ", "   "),
    4: (" 0 ", "/|\\", "   "),
    5: (" 0 ", "/|\\", "/  "),
    6: (" 0 ", "/|\\", "/ \\")
}


def display_hangman(wrong_answers: int) -> None:
    """Print the hangman graphic for the current number of wrong answers."""
    for line in hangman_art[wrong_answers]:
        print(line)


def display_answer(answer: str) -> None:
    """Reveal the correct answer."""
    print(f"The word was: {answer}")


def display_hints(hints: list[str]) -> None:
    """Display the current guessed letters and blanks."""
    print(" ".join(hints))


def main() -> None:
    """Run the hangman game."""
    answer = random.choice(words)
    hints = ["_"] * len(answer)
    wrong_answers = 0
    wrong_guesses: set[str] = set()
    is_running = True

    while is_running:
        display_hangman(wrong_answers)
        display_hints(hints)
        if wrong_guesses:
            print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT.")
            continue

        if guess in hints or guess in wrong_guesses:
            print("You already guessed that.")
            continue

        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hints[i] = guess
            if "_" not in hints:
                print("You win!")
                display_answer(answer)
                is_running = False
        else:
            wrong_answers += 1
            wrong_guesses.add(guess)
            if wrong_answers >= 6:
                display_hangman(wrong_answers)
                print("You lose!")
                display_answer(answer)
                is_running = False


if __name__ == "__main__":
    main()

