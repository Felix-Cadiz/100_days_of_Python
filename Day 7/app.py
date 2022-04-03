import random
from hangman_art import stages, logo
from hangman_words import word_list

# Starting Parameters
random_word = random.choice(word_list)
game_over = False
display = []
guessed = []
lifes = 6
print(logo)
# print(f"The answer is {random_word}")

# Word display
word_length = len(random_word)
for space in range(word_length):
    display += "_"
print(display)

# Guessing Logic
while not game_over:
    guess = input("Guess a letter:\n").lower()
    if guess not in guessed:
      for index in range(word_length):
          letter = random_word[index]
          if letter == guess:
              display[index] = letter
              guessed += guess
      if guess not in display:
          lifes -= 1
          guessed += guess
          if lifes >= 2:
            print(f"{guess} is not in the selected word. Pick another letter! You have {lifes} lifes left.")
          else:
            print(f"{guess} is not in the selected word. Pick another letter! You have {lifes} life left.")
    else: 
      print(f'You have already guessed "{guess}". Pick another letter.')

# Status Summary
    print(stages[lifes])
    print(f"{' '.join(display)}")

# End Game Logic
    if lifes == 0:
        game_over = True
        print("You lose! =(\nGame Over!")

    if "_" not in display:
        game_over = True
        print("You win! =)\nGame Over!")