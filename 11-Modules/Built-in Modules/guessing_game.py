import random
import sys

first = sys.argv[1]
last = sys.argv[2]

true_number = random.randint(int(first), int(last))


print(true_number)

is_true = False
guess_count = 0
while not is_true:
	guess_count += 1
	guess_number = input(f"Please guess a number between {first} and {last} or 'q' to exit :")
	if int(guess_number) == int(true_number):
		is_true = True
		print(f"Great! Your used {guess_count} times to win the game!")
	elif guess_number == 'q':
		print("GoodBye! See you next time.")
		break
	else:
		print("Not the right number! Try again!!")
		continue



