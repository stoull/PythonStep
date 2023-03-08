import random



def checkoutAnswer(guesAnswer, answer):
	if 0 < guesAnswer < 10:
		if guesAnswer == answer:
			return True
		else:
			return False
	else:
		print("I said between 0~10")
		return False




if __name__ == '__main__':
	randomAnswer = random.randint(0, 10)
	while True:
		try:
			guessInt = int(input("Guess a number between 0 ~ 10:"))
			if checkoutAnswer(guessInt, randomAnswer) == True:
				print("You are right")
				break
		except ValueError:
			print("I said the number between 0 ~ 10")
			continue
