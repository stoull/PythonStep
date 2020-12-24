class PlayerCharacter:
	# Class object Attribute
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
			self.age = age

	def shout(self):
		print(f'my name is {self.name}')

player1 = PlayerCharacter('Jane', 27)
player2 = PlayerCharacter('Kevin', 30)

player1.afdfda = 32 # Here's no error through although class PlayerCharacter has no this attribute

print(player1.afdfda) # Your can use this attribute
# help(player1)

print(player1.membership)
print(player2.membership)

player1.shout()
player2.shout()

print(dir(player1))

