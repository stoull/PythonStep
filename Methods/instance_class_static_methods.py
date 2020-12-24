
# Show what's differ between Instance, Class and Static mehtods
import math
# Class methods and static methods
class Pizza:
	def __init__(self, radius, ingredients):
		self.ingredients = ingredients
		self.radius = radius

	def __repr__(self):
		return (f'Pizza(radius: {self.radius!r}),{self.ingredients!r}')

	def area(self):
		return self.circle_area(self.radius)

	@classmethod
	def margherita(cls):
		return cls(4, ['mozzarella', 'tomatoes'])

	@classmethod
	def prosciutto(cls):
		return cls(4, ['mozzarella', 'tomatoes', 'ham'])

	@staticmethod
	def circle_area(r):
		return r ** 2 *math.pi

margheriate1 = Pizza.margherita()

prosciutto1 = Pizza.prosciutto()

print(margheriate1)
print(prosciutto1)

print(margheriate1.area())
print(Pizza.circle_area(4))





	
