import random

def run_guess(guess, answer):
	if 0 < guess < 11:
		if guess == answer:
			print("You're right!!")
			return True
	else:
		print('hey bozo, I said 1~11')
		return False

if __name__ == '__main__':
	answer = random.randint(1, 10)
	while True:
		try:
			guess = int(input("guess a number 1~10: "))
			if (run_guess(guess, answer) == True):
				break
		except ValueError:
			print('Please enter a number')
			continue