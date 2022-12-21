from plus import show
#from replit import clear

import random

word_list = ["book", "keyboard", "orange"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
guesses = []
num_of_try = []

print(f'Pssst, the solution is {chosen_word}.')

for _ in range(word_length):
    display += "_"

end_of_game = False
fail = 0

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in num_of_try:   
      #clear()  
      print("You already entered this letter, try another one.")
      fail += 1
    else:     
      #clear()
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
      if not guess in chosen_word:
          print("Wrong word, try another one.")
          fail += 1
    num_of_try += guess      

    print(display)
    print(show(fail))

    if fail == 6:
      end_of_game = True
      print("GAME OVER")

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
