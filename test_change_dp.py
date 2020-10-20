'''Unittest for change_dp function'''

import unittest
from change_dp import get_change

class FunctionTest(unittest.TestCase):
    ''' testing the change_dp function'''

    def test_1(self):
        m = 100
        c = [10]
        self.assertEqual(get_change(m, c), 10)

    def test_2(self):
        m = 0
        c = [1, 2, 3]
        self.assertEqual(get_change(m, c), 0)

    def test_3(self):
        m = 18
        c = [10 , 4]
        self.assertEqual(get_change(m, c), 3)

if __name__ == '__main__':
    unittest.main()
