class Cat:
	isAnimal = True
	def __init__(self, name, age, sex = "male"):
		self.name = name
		self.age = age
	def catch_mouse(self):
		print(f"cat {self.name} is catching a mouse")

	@classmethod
	def show_miaow(cls):
		print("This is the miaow example of cats")

	# Use class method create a new intance
	@classmethod
	def female_cat(cls):
		return cls("No_Name", 3, "Femal")

	# static method has no param of cls
	@staticmethod
	def show_run_example():
		print("This a example of running of cats")

Cat.show_miaow()

cat_kevin = Cat("Kevin", 30)

cat_kevin.catch_mouse()

# Using class method to create a female cat
a_female_cat = Cat.female_cat()
a_female_cat.catch_mouse()


# static method
Cat.show_run_example()