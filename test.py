# This file contains all the testcases of week2 questions
# Authors: Cédric Murairi, Mthabisi Ndlovu, Samuel Anumudu
# Thursday, 21 January 2021

import implementation as im
import unittest as ut

class TrimTest(ut.TestCase):

    def test_left_trim(self):
        self.assertEqual(im.remove_extra_spaces("   Hello there I am Tony"), "Hello there I am Tony")

    def test_right_trim(self):
        self.assertEqual(im.remove_extra_spaces("Hello there I am Tony     "), "Hello there I am Tony")

    def test_both(self):
        self.assertEqual(im.remove_extra_spaces("    Hello    there I   am Tony     "), "Hello there I am Tony")

class CountCharsTest(ut.TestCase):
    
    def test_simple_str(self):
        self.assertEqual(im.count_chars("Hello folks")['l'], 3)

    def test_mid_str(self):
        self.assertIn(',', im.count_chars("Hello there, I am cedric").keys())

    def test_complex_str(self):
        self.assertFalse('-' not in im.count_chars("Outlandish-fantastic"))

class NestedListTest(ut.TestCase):

    def test_duplicate(self):
        self.assertTrue(im.nested_list_to_list([[1, 2, 30], [2, 3, 4], [1, 4, 5]]).count(4) == 1)

class FindMissingTest(ut.TestCase):

    def test_missing_result(self):
        self.assertListEqual(im.find_missing([1, 2, 4, 5], [1, 4, 5]), [2])

    def test_equal_lists(self):
        self.assertTrue(not im.find_missing([1, 2, 3], [1, 2, 3]))

class UnpackingTest(ut.TestCase):

    def test_occurrence(self):
        self.assertEqual(im.unpack_int_to_list(10).count(10), 10)

    def test_list_size(self):
        # self.assert
        pass

if __name__ == "__main__":
    ut.main()
