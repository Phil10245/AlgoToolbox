import unittest

from edit_distance import edit_distance

class TestEditDist (unittest.TestCase):
    '''Testing the edit_distance function'''

    def test_edit_dist_empty_str(self):
        string_a = ""
        string_b = "abc"
        self.assertEqual(edit_distance(string_a, string_b), 3)

    def test_edit_dist_same(self):
        string_a = "abc"
        string_b = "abc"
        self.assertEqual(edit_distance(string_a, string_b), 0)

    def test_edit_dist_one_ch_match(self):
        string_a = "a"
        string_b = "a"
        self.assertEqual(edit_distance(string_a, string_b), 0)

    def test_edit_dist_one_ch_mismatch(self):
        string_a = "a"
        string_b = "b"
        self.assertEqual(edit_distance(string_a, string_b), 1)

    def test_edit_dist_two_ch_match(self):
        string_a = "ab"
        string_b = "ab"
        self.assertEqual(edit_distance(string_a, string_b), 0)

    def test_edit_dist_two_ch_ins(self):
        string_a = "a"
        string_b = "ab"
        self.assertEqual(edit_distance(string_a, string_b), 1)

    def test_edit_dist_long(self):
        string_a = "abcdefghijklmnop"
        string_b = "abfghjaqoisakvxmp"
        self.assertEqual(edit_distance(string_a, string_b), 13)

    def test_edit_3(self):
        string_a = "abcd"
        string_b = "abfh"
        self.assertEqual(edit_distance(string_a, string_b), 2)

    def test_edit_dist_1(self):
        string_a = "zettel"
        string_b = "yaethel"
        self.assertEqual(edit_distance(string_a, string_b), 3)

    def test_edit_dist_2(self):
        string_a = "editing"
        string_b = "distance"
        self.assertEqual(edit_distance(string_a, string_b), 5)


if __name__ == '__main__':
    unittest.main()
