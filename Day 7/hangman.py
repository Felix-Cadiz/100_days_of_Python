import random

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
print(f"The answer is {random_word}")
display = []
lives = 5
game_over = False

word_length = len(random_word)
for space in range(word_length):
    display += "_"
print(display)

while not game_over:
    guess = input("Guess a letter:\n").lower()
    # print(guess)

    for index in range(word_length):
        letter = random_word[index]
        if letter == guess:
            display[index] = letter

    print(display)

    if "_" not in display:
        game_over = True
        print("You win! Game Over!")