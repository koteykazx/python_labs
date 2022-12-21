word_list = ["book", "keyboard", "orange"]

import random
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in chosen_word:
  display.append("_")
print(display)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        display[chosen_word.index(letter)] = letter

print(display)
