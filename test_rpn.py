import unittest
import rpn


class TestBasics(unittest.TestCase):

    def test_add(self):

        self.assertEqual(2,rpn.calculate('1 1 +'))
        self.assertEqual(4,rpn.calculate('1 1 1 1 +'))
        self.assertEqual(0,rpn.calculate('1 -1 2 -2 +'))
        self.assertEqual(0,rpn.calculate('0 0 +'))
        self.assertEqual(-3,rpn.calculate('4 -5 -2 +'))
        self.assertEqual(9,rpn.calculate('1 2 + 4 + 2 +'))
        self.assertEqual(-4,rpn.calculate('0 0 + 2 + -3 -1 + -2 +'))
        print('Passed add test')

    def test_minus(self):
        self.assertEqual(2, rpn.calculate('4 2 -'))

if __name__ == '__main__':

    test = TestBasics()
    test.test_add()
    test.test_minus()
