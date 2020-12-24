import unittest

class TestMain(unittest.TestCase):
	"""docstring for TestMain"""

	def test_1_to_10(self):
		for i in range(1, 11):
			resut = guessing_game(i)
			pass


if __name__ == '__main__':
	unittest.main()
	
