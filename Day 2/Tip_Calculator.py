# Day 2 of Angela Yu's "100 Days of Python" on udemy.

print("Welcome to the Tip Calculator")

total = float(input("What was the total bill \n"))

tip = (total * (0.01 * int(input("What percentage tip would you like to give? 10, 12, 15, or custom? \n"))))

split = int(input("How many people are you splitting the bill with\n"))

individual_Cost = "{:.2f}".format((total + tip) / split)

print(f"Each person should pay: ${individual_Cost}")