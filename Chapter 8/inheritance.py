class User():
	"""docstring for User"""
	def __init__(self, name):
		self.name = name

	def log_in(self):
		print(f"{name} has logged in")

	def attack(self):
		print("Doing nothing!")

class Wizard(User):
	"""docstring for Wizard"""
	def __init__(self, power):
		super(Wizard, self).__init__("Wizard")
		self.power = power
		
	def attack(self):
		print(f"wizard {self.name} is attacking with power of {self.power}")

class Archer(User):
	def __init__(self, num_arrows):
		super(Archer, self).__init__("Archer")
		self.num_arrows =  num_arrows

	def attack(self):
		print(f"archer {self.name} is attacking with arrows left: {self.num_arrows}")


wizard1 = Wizard(80)
archer1 = Archer(100)

wizard1.log_in
archer1.log_in

wizard1.attack()
archer1.attack()




