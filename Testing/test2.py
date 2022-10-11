import unittest
from random import randint
import script


class TestScript(unittest.TestCase):
    def test1(self):
        res = script.check_guess(7, 7)
        self.assertTrue(res)

    def test2(self):
        new_result = script.check_guess(40, 10)
        self.assertEqual(new_result, False)


if __name__ == '__main__':
    unittest.main()
