
import unittest
import main
class TestMain(unittest.TestCase):
	"""docstring for TestMain"""
	
	def setUp(self):
		print("Here is to set up")

	def tearDown(self):
		print("Do cleaning jobs")

	def test_do_stuff(self):
		"""Testing for a Integer number"""
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		"""Testing for a string"""
		test_param = 'shshskd'
		result = main.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		"""Testing for a value of None"""
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, "Please input a number")

if __name__ == '__main__':
	unittest.main()


"""
try this command:
python3 -m unittest 	# This will run all the test under the same directory

or this:
python3 -m unittest -v  # This will give more information

"""