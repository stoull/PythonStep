
import unittest
import main
class TestMain(unittest.TestCase):
	"""docstring for TestMain"""
	
	def test_do_stuff(self):
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'shshskd'
		result = main.do_stuff(test_param)
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
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