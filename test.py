# This file contains all the testcases of week2 questions
# Authors: Cédric Murairi, Mthabisi Ndlovu, Samuel Anumudu
# Thursday, 21 January 2021

import implementation as im
import unittest as ut

class TrimTest(ut.TestCase):

    def test_left_trim(self):
        self.assertEqual(im.custom_trim("   Hello there I am Tony"), "Hello there I am Tony")

    def test_right_trim(self):
        self.assertEqual(im.custom_trim("Hello there I am Tony     "), "Hello there I am Tony")

    def test_both(self):
        self.assertEqual(im.custom_trim("    Hello    there I   am Tony     "), "Hello there I am Tony")

class OccurrenceTest(ut.TestCase):
    
    def test_simple_str(self):
        self.assertEqual(im.find_occurence("Hello folks")['l'], 3)

    def test_mid_str(self):
        self.assertIn(',', im.find_occurence("Hello there, I am cedric").keys())

    def test_complex_str(self):
        self.assertFalse('-' not in im.find_occurence("Outlandish-fantastic"))

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
