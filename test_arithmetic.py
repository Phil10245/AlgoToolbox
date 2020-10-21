'''Unittest for arithmetic function'''

import unittest
import arithmetic

class TestPara(unittest.TestCase):
    ''' testing the placing_parantheses_pmu function'''

    def test_evalt1(self):
        ''' (3,3, "+") -> 6'''
        self.assertEqual(arithmetic.evalt(3,3,"+"), 6)


    def test_1(self):
        ''' "2+2*2" -> 8'''
        exp = "2+2*2"
        self.assertEqual(arithmetic.get_maximum_value(exp), 8)

    def test_2(self):
        ''' "5-8+7*4-8+9" -> 200'''
        exp = "5-8+7*4-8+9"
        self.assertEqual(arithmetic.get_maximum_value(exp), 200)

    def test_3(self):
        ''' "5+1" -> 6 '''
        self.assertEqual(arithmetic.get_maximum_value("5+1"), 6)

    def test_max(self):
        '''testing max'''
        exp="5+9-7*3+7*6*4-9-2+4+9*4+6+7+9"
        print(arithmetic.get_maximum_value(exp))

if __name__ == '__main__':
    unittest.main()
