
# Using Yield to caculate fibonacci list
def fib(number):
	a = 0
	b = 1

	for i in range(number):
		yield a
		temp = a
		a = b
		b = b + temp

for i in fib(4):
	print(f"i is : {i}")


print("Using Yield to caculate fibonacci list")
print(list(fib(21)))


# 用Generator Dunder mehtods 求 fibonacci 数列
print(f"用Generator 求 fibonacci 数列")

class Fibonacci():
	def __init__(self, last):
		self.last = last
		self.current = 0

		self.current_total = 0
		self.previous_total = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.current == 0:
			pass
		elif self.current == 1:
			self.current_total = 1
		elif self.current < self.last:
			new_total = self.current_total + self.previous_total
			self.previous_total = self.current_total
			self.current_total = new_total
		elif self.current >= self.last:
			raise StopIteration
		else:
			raise "Unacceptable number"
		self.current += 1
		return self.current_total


alist = list(Fibonacci(21))
print(alist)


# 函数递归求 fibonacci 数列
print(f"函数递归求 fibonacci 数列的例子")
def fibonacci(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(20))