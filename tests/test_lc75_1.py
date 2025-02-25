"""Tests for easy.py
"""
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lc75_1 import LC75EasyArrays, LC75MediumArrays, LC75EasyTwoPointers, LC75EasyPrefixSum


class TestLC75EasyArrays(unittest.TestCase):
  """Tests for easy.py
  """

  def test_merge_alternately(self):
    """Test merge_alternately
    """
    self.assertEqual(LC75EasyArrays().merge_alternately("abc", "pqr"), "apbqcr")
    self.assertEqual(LC75EasyArrays().merge_alternately("ab", "pqrs"), "apbqrs")
    self.assertEqual(LC75EasyArrays().merge_alternately("abcd", "pq"), "apbqcd")

  def test_gcd_of_strings(self):
    """Test gcd_of_strings
    """
    self.assertEqual(LC75EasyArrays().gcd_of_strings("AAAAAAAAA", "AAAA"), "A")
    self.assertEqual(LC75EasyArrays().gcd_of_strings("ABCABC", "ABC"), "ABC")
    self.assertEqual(LC75EasyArrays().gcd_of_strings("ABABAB", "ABAB"), "AB")
    self.assertEqual(LC75EasyArrays().gcd_of_strings("ABABABAB", "ABAB"), "ABAB")
    self.assertEqual(LC75EasyArrays().gcd_of_strings("LEET", "CODE"), "")

  def test_kids_with_candies(self):
    """Test Kids with candies
    """
    self.assertEqual(LC75EasyArrays().kids_with_candies([2,3,5,1,3], 3), [True,True,True,False,True])
    self.assertEqual(LC75EasyArrays().kids_with_candies([4,2,1,1,2], 1), [True,False,False,False,False])
    self.assertEqual(LC75EasyArrays().kids_with_candies([12,1,12], 10), [True,False,True])

  def test_can_place_flowers(self):
    """Test can_place_flowers
    """
    self.assertTrue(LC75EasyArrays().can_place_flowers([1], 0))
    self.assertFalse(LC75EasyArrays().can_place_flowers([1], 1))
    self.assertTrue(LC75EasyArrays().can_place_flowers([0], 1))
    self.assertTrue(LC75EasyArrays().can_place_flowers([1,0,0,0,0], 2))
    self.assertTrue(LC75EasyArrays().can_place_flowers([1,0,0,0,1], 1))
    self.assertTrue(LC75EasyArrays().can_place_flowers([1,0,0,0,1,0,0], 0))
    self.assertFalse(LC75EasyArrays().can_place_flowers([1,0,0,0,1], 2))
    self.assertFalse(LC75EasyArrays().can_place_flowers([1,0,0,0,0,1], 2))

  def test_reverse_vowels(self):
    """Test reverse_vowels
    """
    tuples = [
      ("hello", "holle"),
      ("leetcode", "leotcede"),
      ("aA", "Aa"),
      ("a", "a"),
      ("A", "A"),
      ("", ""),
      ("racecar", "racecar"),
      ("aAeEiIoOuU", "UuOoIiEeAa"),    ]
    for t in tuples:
      self.assertEqual(LC75EasyArrays().reverse_vowels(t[0]), t[1])

class TestLC75MediumArrays(unittest.TestCase):
  """Tests for medium arrays solutions
  """

  def test_reverse_words(self):
    """Test reverse_words
    """
    self.assertEqual(LC75MediumArrays().reverse_words("Let's take LeetCode contest"), "contest LeetCode take Let's")
    self.assertEqual(LC75MediumArrays().reverse_words("God  Ding "), "Ding God")
    self.assertEqual(LC75MediumArrays().reverse_words(" Hello World  "), "World Hello")

  def test_product_except_self(self):
    """Test product_except_self
    """
    self.assertEqual(LC75MediumArrays().product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    self.assertEqual(LC75MediumArrays().product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
    self.assertEqual(LC75MediumArrays().product_except_self([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    self.assertEqual(LC75MediumArrays().product_except_self([1, 2, 3, 4, 5, 6]), [720, 360, 240, 180, 144, 120])

class TestLC75EasyTwoPointers(unittest.TestCase):
  """Tests for two pointers solutions
  """

  def test_move_zeroes(self):
    """Test move_zeroes
    """
    test_sets = [
      ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
      ([0], [0]),
      ([1, 0], [1, 0]),
      ([1, 0, 1], [1, 1, 0]),
      ([0, 1, 0], [1, 0, 0]),
      ([0, 0, 1], [1, 0, 0]),
    ]
    for test_set in test_sets:
      nums = test_set[0].copy() # copy to avoid changing the original list
      LC75EasyTwoPointers().move_zeroes(nums)
      self.assertEqual(nums, test_set[1])

  def test_is_subsequence(self):
    """Test is_subsequence
    """
    test_sets = [
      ("abc", "ahbgdc", True),
      ("axc", "ahbgdc", False),
      ("", "ahbgdc", True),
      ("ahbgdc", "ahbgdc", True),
      ("aaaaaaaa", "bbaaaa", False),
      ("abc", "", False),
      ("", "", True),
      ("a", "a", True),
      ("a", "b", False),
      ("a", "ab", True),
      ("ab", "ba", False),
      ("ab", "abc", True),
      ("abc", "acb", False),
      ("abc", "cab", False),
      ("abc", "cba", False),
      ("abc", "bca", False),
      ("abc", "bac", False),
      ("abc", "abc", True),
      ("abc", "abcd", True),
      ("abc", "ab", False),
      ("abc", "a", False),
      ("abc", "b", False),
      ("abc", "c", False),
      ("abc", "d", False),
      ("abc", "e", False),
      ("abc", "f", False),
      ("abc", "g", False),
      ("abc", "h", False),
      ("abc", "i", False),
      ("abc", "j", False),
      ("abc", "k", False),
      ("abc", "l", False),
      ("abc", "m", False),
      ("abc", "n", False),
      ("abc", "o", False),
      ("abc", "p", False),
      ("abc", "q", False),
      ("abc", "r", False),
      ("abc", "s", False),
      ("abc", "t", False),
      ("abc", "u", False),
      ("abc", "v", False),
      ("abc", "w", False),
      ("abc", "x", False),
      ("abc", "y", False),
      ("abc", "z", False),
    ]
    for test_set in test_sets:
      self.assertEqual(LC75EasyTwoPointers().is_subsequence(test_set[0], test_set[1]), test_set[2])

class TestLC75EasyPrefixSum(unittest.TestCase):
  """Tests for prefix sum solutions
  """

  def test_largest_altitude(self):
    """Test largest_altitude
    """
    self.assertEqual(LC75EasyPrefixSum().largest_altitude(
      [-5, 1, 5, 0, -7]), 1)
    self.assertEqual(LC75EasyPrefixSum().largest_altitude(
      [-4, -3, -2, -1, 4, 3, 2]), 0)
    self.assertEqual(LC75EasyPrefixSum().largest_altitude(
      [-5, 1, 5, 0, -7, 2, -3, 4, -2, 1, -1, 6]), 1)
    self.assertEqual(LC75EasyPrefixSum().largest_altitude(
      [-5, 1, 5, 0, -7, 2, -3, 4, -2, 1, -1, 6, -5, 1, 5, 0, -7, 2, -3, 4, -2, 1, -1, 6]), 2)

if __name__ == "__main__":
    unittest.main()
