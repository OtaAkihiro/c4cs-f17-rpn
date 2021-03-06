
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
        print('Passed minus test')

    def test_exp(self):
        self.assertEqual(4, rpn.calculate('2 2 ^'))
        self.assertEqual(8, rpn.calculate('2 3 ^'))
        print('Passed exp test')

    def test_div(self):
        self.assertEqual(6, rpn.calculate('12 2 /'))
        self.assertEqual(8, rpn.calculate('16 2 /'))
        self.assertEqual(1, rpn.calculate('12 4 / 3 /'))

if __name__ == '__main__':

    test = TestBasics()
    test.test_add()
    test.test_minus()
    test.test_exp()
    test.test_div()
