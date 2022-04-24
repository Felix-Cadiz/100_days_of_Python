# Debugging Exercises from Angela Yu's "100 days of python" on Udemy.

############DEBUGGING#####################

# Describe Problem - Include the end of the range on line 21.
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug - Alter randint to include index 0 on line 15.
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer - >= 1994 on line 22.
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors - Int on line 25, indentation on line 28, f string on line 28.
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend - Removed extra "=" on line 34
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger - Indentation on line 43
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])