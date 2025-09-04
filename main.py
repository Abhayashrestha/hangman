import random

# random module is used to select random words from the list
words = ["apple", "banana", "cherry", "mango", "litchi", "orange", "grape"]

# creating ASCII art for the hangman representation
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" 0 ", "   ", "   "),
    2: (" 0 ", " | ", "   "),
    3: (" 0 ", "/| ", "   "),
    4: (" 0 ", "/|\\", "   "),
    5: (" 0 ", "/|\\", "/  "),
    6: (" 0 ", "/|\\", "/ \\"),
}


def display_hangman(wrong_answers: int) -> None:
    """Print the hangman ASCII art for the given number of wrong answers."""
    for line in hangman_art[wrong_answers]:
        print(line)


def display_answer(answer: str) -> None:
    """Reveal the answer to the player."""
    print(f"The word was: {answer}")


def display_hints(hints: list[str]) -> None:
    """Print the current hint representation of the word."""
    print(" ".join(hints))


def main() -> None:
    answer = random.choice(words)
    hints = ["_"] * len(answer)
    wrong_answers = 0
    wrong_guesses: set[str] = set()

    while True:
        display_hangman(wrong_answers)
        display_hints(hints)
        if wrong_guesses:
            print(f"Wrong guesses: {' '.join(sorted(wrong_guesses))}")

        guess = input("Enter your guess: ").lower()

        if len(guess) > 1:
            if guess == answer:
                hints = list(answer)
                print("You guessed the word!")
                break
            else:
                print("Wrong word guess.")
                wrong_answers += 1
        elif len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT.")
            continue
        elif guess in wrong_guesses or guess in hints:
            print("You already guessed that.")
            continue
        elif guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hints[i] = guess
        else:
            wrong_guesses.add(guess)
            wrong_answers += 1

        if "_" not in hints:
            print("Congratulations! You win!")
            break
        if wrong_answers == max(hangman_art.keys()):
            print("Game Over!")
            break

    display_hangman(wrong_answers)
    display_hints(hints)
    display_answer(answer)


if __name__ == "__main__":
    main()

