import unittest
import main

# to run all tests at the same time for multiple modules, python3 -m unittest in terminal
# to get detailed info on result of each test, python3 -m unittest -v


class mainTester(unittest.TestCase):  # inherit from unittest parent class
    def setUp(self):
        # executes before each test method call(default method as part of Unittest class)
        print("Testing the function")

    def test_function(self):
        param1, param2 = 2, 4
        # passing parameters into function being tested in main
        res = main.calc_pow(param1, param2)
        # checking if the function returns a value equal to what's expected
        self.assertEqual(res, 16)

    def test_function2(self):
        param3, param4 = 'nfgsa', 5
        newRes = main.calc_pow(param3, param4)
        # function returns err that is an instance of ValueError class
        self.assertIsInstance(newRes, ValueError)

    def test_function3(self):
        param5, param6 = 'sdfs', '25w4q2w34'
        newRes2 = main.calc_pow(param5, param6)
        self.assertTrue(isinstance(newRes2, ValueError))

    def test_function4(self):
        newparam, newparam2 = None, None
        result = main.calc_pow(newparam, newparam2)
        self.assertEqual(result, 'Both need to be a number')

    def tearDown(self):
        # default method that executes after a test method call(opposite of setUp)
        print("Cleaning up")


if __name__ == '__main__':
    unittest.main()
