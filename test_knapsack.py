from knapsack import optimal_weight
import unittest

class TestKnapSack(unittest.TestCase):

    def test_equal(self):
        capacity = 1
        goldbars_weight = [3, 2, 1]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 1)

    def test_equal2(self):
        capacity = 1
        goldbars_weight = [2]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 0)

    def test_equal3(self):
        capacity = 2
        goldbars_weight = [1, 5, 1]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 2)

    def test_equal4(self):
        capacity = 5
        goldbars_weight = [1, 3, 4]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 5)

    def test_equal5(self):
        capacity = 10
        goldbars_weight = [9, 7, 3]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 10)

    def test_equal6(self):
        capacity = 10
        goldbars_weight = [1,1,1,1,1,1]

        self.assertEqual(optimal_weight(capacity, goldbars_weight), 6)


if __name__ == '__main__':
    unittest.main()
