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
    pass

def display_hints(hints):
    print(" ".join(hints))
#main method to run the game
def main():
    answer=random.choice(words)
    hints=["_"]*len(answer)
    wrong_answers=0
    wrong_guesses=set()
    is_running = True

    while is_running:
      display_hangman(wrong_answers)
      display_hints(hints)
      guess=input("Enter your guess: ").lower()

      if len (guess)!=1 or not guess.isalpha():
         print("INVALID INPUT .")
         continue


      if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
                hints[i] = guess



if __name__ == "__main__":
   main()
