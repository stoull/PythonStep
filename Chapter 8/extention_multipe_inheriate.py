# extending a built-in class 'list'
class SuperList(list):

	def __len__(self):
		return 100


super_list1 = SuperList();
print(len(super_list1))

super_list1.append(5)
print(super_list1[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))

import keyword
print(keyword.iskeyword('list'))


# inheriate multiple class

class User():
	def __init__(self, name):
		self.name = name

	def log_in(self):
		print(f"{self.name} has logged in")
		pass
class Wizard(User):
	def __init__(self, power):
		super().__init__("wizard")
		self.power = power

	def attack(self):
		print(f"{self.name} attacking with power: {self.power}")

class Archer(User):
	"""docstring for Archer"""
	def __init__(self, arrows):
		super(Archer, self).__init__("archer")
		self.arrows = arrows

	def check_arrows(self):
		print(f"{self.name} has {self.arrows} arrows")

	def run(self):
		print(f"{self.name} run really fast!")

# A class inheriate classes Wizard and Archer
class HybridBorg(Wizard, Archer, User):
			"""docstring for HybridBorg"""
			def __init__(self, enhance_power, power, arrows):
				Wizard.__init__(self, power)
				Archer.__init__(self, arrows)
				# User.__init__(self, "HybridBorg")
				self.name = "hybridborg"
				self.enhance_power = enhance_power

			def attack(self):
				print(f"{self.name} is attacking with power: {self.power + self.enhance_power}")


wizard1 = Wizard(82)
archer1 = Archer(100)

wizard1.attack()
archer1.check_arrows()

# 

hybrid_borg1 = HybridBorg(50, 80, 800)
hybrid_borg1.log_in()

hybrid_borg1.run()
hybrid_borg1.check_arrows()
hybrid_borg1.attack()


print(f"Character name is '{hybrid_borg1.name}'")



