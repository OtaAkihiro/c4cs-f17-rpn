import unittest
import rpn

print('testing')


class TestBasics(unittest.TestCase):

    def test_add(self):

        self.assertEqual(2, '1 1 +')
        self.assertEqual(4, '1 1 1 1 +')
        self.assertEqual(7, '1 2 3 1 +')
        self.assertEqual(0, '1 -1 2 -2 +')
        self.assertEqual(0, '0 0 +')
        self.assertEqual(-3, '4 -5 -2 +')
        self.assertEqual(9, '1 2 + 4 + 2 +')
        self.assertEqual(-4, '0 0 + 2 + -3 -1 + -2 +')
        

if __name__ == '__main__':

    test = TestBasics()
    test.test_add()
