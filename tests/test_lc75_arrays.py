"""Tests for easy.py
"""
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lc75_arrays import LC75ArraysEasy, LC75ArraysMedium


class TestLC75ArraysEasy(unittest.TestCase):
  """Tests for easy.py
  """

  def test_merge_alternately(self):
    """Test merge_alternately
    """
    self.assertEqual(LC75ArraysEasy().merge_alternately("abc", "pqr"), "apbqcr")
    self.assertEqual(LC75ArraysEasy().merge_alternately("ab", "pqrs"), "apbqrs")
    self.assertEqual(LC75ArraysEasy().merge_alternately("abcd", "pq"), "apbqcd")

  def test_gcd_of_strings(self):
    """Test gcd_of_strings
    """
    self.assertEqual(LC75ArraysEasy().gcd_of_strings("AAAAAAAAA", "AAAA"), "A")
    self.assertEqual(LC75ArraysEasy().gcd_of_strings("ABCABC", "ABC"), "ABC")
    self.assertEqual(LC75ArraysEasy().gcd_of_strings("ABABAB", "ABAB"), "AB")
    self.assertEqual(LC75ArraysEasy().gcd_of_strings("ABABABAB", "ABAB"), "ABAB")
    self.assertEqual(LC75ArraysEasy().gcd_of_strings("LEET", "CODE"), "")

  def test_kids_with_candies(self):
    """Test Kids with candies
    """
    self.assertEqual(LC75ArraysEasy().kids_with_candies([2,3,5,1,3], 3), [True,True,True,False,True])
    self.assertEqual(LC75ArraysEasy().kids_with_candies([4,2,1,1,2], 1), [True,False,False,False,False])
    self.assertEqual(LC75ArraysEasy().kids_with_candies([12,1,12], 10), [True,False,True])

  def test_can_place_flowers(self):
    """Test can_place_flowers
    """
    self.assertTrue(LC75ArraysEasy().can_place_flowers([1], 0))
    self.assertFalse(LC75ArraysEasy().can_place_flowers([1], 1))
    self.assertTrue(LC75ArraysEasy().can_place_flowers([0], 1))
    self.assertTrue(LC75ArraysEasy().can_place_flowers([1,0,0,0,0], 2))
    self.assertTrue(LC75ArraysEasy().can_place_flowers([1,0,0,0,1], 1))
    self.assertTrue(LC75ArraysEasy().can_place_flowers([1,0,0,0,1,0,0], 0))
    self.assertFalse(LC75ArraysEasy().can_place_flowers([1,0,0,0,1], 2))
    self.assertFalse(LC75ArraysEasy().can_place_flowers([1,0,0,0,0,1], 2))

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
      self.assertEqual(LC75ArraysEasy().reverse_vowels(t[0]), t[1])

class TestLC75ArraysMedium(unittest.TestCase):
  """Tests for medium arrays solutions
  """

  def test_reverse_words(self):
    """Test reverse_words
    """
    self.assertEqual(LC75ArraysMedium().reverse_words("Let's take LeetCode contest"), "contest LeetCode take Let's")
    self.assertEqual(LC75ArraysMedium().reverse_words("God  Ding "), "Ding God")
    self.assertEqual(LC75ArraysMedium().reverse_words(" Hello World  "), "World Hello")

  def test_product_except_self(self):
    """Test product_except_self
    """
    self.assertEqual(LC75ArraysMedium().product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    self.assertEqual(LC75ArraysMedium().product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
    self.assertEqual(LC75ArraysMedium().product_except_self([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
    self.assertEqual(LC75ArraysMedium().product_except_self([1, 2, 3, 4, 5, 6]), [720, 360, 240, 180, 144, 120])

if __name__ == "__main__":
    unittest.main()
