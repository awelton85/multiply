"""
A simple multiplication game that allows the user to practice a specific table.
"""

import random

table = int(input("Hi Henry, which table would you like to practice? "))
right = 0
wrong = 0


def make_problem(number):
	"""Generates a multiplication problem and returns the user's answer,
	the upper number, and the lower number."""
	upper = random.randint(0, 9)
	lower = number
	user_input = input(f"\n  {upper}\nX {lower}\n")
	return user_input, upper, lower


while True:
	answer = make_problem(table)
	try:
		if str(answer[0]) == "":
			print("You didn't enter a number!")

		elif str(answer[0]) == "q".lower():
			print(f"Your final score is: {right} out of {right + wrong}\nGreat job, Goose!")
			break
		elif int(answer[0]) == int(answer[1]) * int(answer[2]):
			right += 1
			print("Correct!")
		elif int(answer[0]) != int(answer[1]) * int(answer[2]):
			wrong += 1
			print(f"Incorrect. The answer is {answer[1] * answer[2]}")
		print(f"You have answered {right} out of {right + wrong} correctly.")
		print("Enter 'q' to quit")
	except ValueError:
		print("You entered something weird.")
