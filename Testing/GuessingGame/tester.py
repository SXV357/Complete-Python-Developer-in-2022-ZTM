import unittest
import Script


class TestGame(unittest.TestCase):
    def test_1(self):
        res = Script.check_guess(5, 5)
        self.assertTrue(res)

    def test_2(self):
        res = Script.check_guess(15, 7)
        self.assertFalse(res)

    def test_3(self):
        res = Script.check_guess('sfsdf', 3)
        self.assertIsInstance(res, TypeError)


if __name__ == '__main__':
    unittest.main()
