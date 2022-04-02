import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
game_over = False
display = []
lives = 6

# print(f"The answer is {random_word}")

word_length = len(random_word)
for space in range(word_length):
    display += "_"
print(display)

while not game_over:
    guess = input("Guess a letter:\n").lower()

    for index in range(word_length):
        letter = random_word[index]
        if letter == guess:
            display[index] = letter
    
    if guess not in display:
        lives -= 1

    print(stages[lives])
    print(f"{' '.join(display)}")

    if lives == 0:
        game_over = True
        print("You lose! =(\nGame Over!")

    if "_" not in display:
        game_over = True
        print("You win! =)\nGame Over!")