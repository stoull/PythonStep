# Here is a helper
from time import time 

class Helper():
	def __init__(self):
		pass

	def performance(fn):
		def warpper(self, *args, **kwargs):
			t1 = time()
			result = fn(*args, **kwargs)
			t2 = time()
			print(f"{fn.__name__} has spend {t2 - t1}s")
			return result
		return warpper

