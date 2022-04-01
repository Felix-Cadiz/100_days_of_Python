import random

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
print(f"The answer is {random_word}")
display = []
lives = 5

word_length = len(random_word)
for space in range(word_length):
    display += "_"
print(display)

# if random_word == display:
#     print("You win!")

guess = input("Guess a letter:\n").lower()
# print(guess)

for index in range(word_length):
    letter = random_word[index]
    if letter == guess:
        display[index] = letter

print(display)