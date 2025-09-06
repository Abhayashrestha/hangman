import random
#random module is used to select random words from the list
words= ["apple","banana","cherry","mango","litchi","orange","grape"]
#creating askii art for the hangman representation
hangman_art= {0:("   "
                 "   "
                 "   "),
               1:(" 0  ",
                  "   ",
                  "   "),
               2:(" 0  ",
                  " |  ",
                  "   "),
                3:(" 0  ",
                   "/|  "
                   "   "),
                4:(" 0  ",
                   "/|\\ ",
                   "   "),
                5:(" 0  ",
                   "/|\\ ",
                   "/   "),
                6:(" 0  ",
                   "/|\\  ",
                   "/ \\  ")}

#creating functions to display hangman, answer, and hints

def display_hangman(wrong_answers):
    for line in hangman_art[wrong_answers]:
         print(line)

def display_answer(answer):
    print(f"The word was: {answer}")

def display_hints(hints):
    print(" ".join(hints))
# display wrong guesses
def display_wrong_guesses(wrong_guesses):
    if wrong_guesses:
        print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
#main method to run the game
def main():
    play_again = True
    while play_again:
        answer=random.choice(words)
        hints=["_"]*len(answer)
        wrong_answers=0
        wrong_guesses=set()

        while True:
            display_hangman(wrong_answers)
            display_hints(hints)
            display_wrong_guesses(wrong_guesses)
            guess=input("Enter your guess: ").lower()

            if len (guess)!=1 or not guess.isalpha():
                print("INVALID INPUT .")
                continue

            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hints[i] = guess
                if "_" not in hints:
                    print("You won!")
                    display_answer(answer)
                    break
            else:
                if guess not in wrong_guesses:
                    wrong_answers += 1
                    wrong_guesses.add(guess)
                else:
                    print("You already guessed that letter.")

                if wrong_answers == max(hangman_art.keys()):
                    display_hangman(wrong_answers)
                    print("You lost!")
                    display_answer(answer)
                    break

        play_again = input("Play again? (y/n): ").lower() == 'y'


if __name__ == "__main__":
   main()
