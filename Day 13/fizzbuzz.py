# Interactive Coding Exercise 3
# Solution - Changed "or" to the "and" operator on line 6
# Altered the "if" statements to "elif" on lines 8 and 10

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])