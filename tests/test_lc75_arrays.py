"""Tests for easy.py
"""
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lc75_arrays import LC75Arrays


class TestLC75(unittest.TestCase):
  """Tests for easy.py
  """

  def test_merge_alternately(self):
    """Test merge_alternately
    """
    self.assertEqual(LC75Arrays().merge_alternately("abc", "pqr"), "apbqcr")
    self.assertEqual(LC75Arrays().merge_alternately("ab", "pqrs"), "apbqrs")
    self.assertEqual(LC75Arrays().merge_alternately("abcd", "pq"), "apbqcd")

  def test_gcd_of_strings(self):
    """Test gcd_of_strings
    """
    self.assertEqual(LC75Arrays().gcd_of_strings("AAAAAAAAA", "AAAA"), "A")
    self.assertEqual(LC75Arrays().gcd_of_strings("ABCABC", "ABC"), "ABC")
    self.assertEqual(LC75Arrays().gcd_of_strings("ABABAB", "ABAB"), "AB")
    self.assertEqual(LC75Arrays().gcd_of_strings("ABABABAB", "ABAB"), "ABAB")
    self.assertEqual(LC75Arrays().gcd_of_strings("LEET", "CODE"), "")

  def test_kids_with_candies(self):
    """Test Kids with candies
    """
    self.assertEqual(LC75Arrays().kids_with_candies([2,3,5,1,3], 3), [True,True,True,False,True])
    self.assertEqual(LC75Arrays().kids_with_candies([4,2,1,1,2], 1), [True,False,False,False,False])
    self.assertEqual(LC75Arrays().kids_with_candies([12,1,12], 10), [True,False,True])

  def test_can_place_flowers(self):
    """Test can_place_flowers
    """
    self.assertTrue(LC75Arrays().can_place_flowers([1], 0))
    self.assertFalse(LC75Arrays().can_place_flowers([1], 1))
    self.assertTrue(LC75Arrays().can_place_flowers([0], 1))
    self.assertTrue(LC75Arrays().can_place_flowers([1,0,0,0,0], 2))
    self.assertTrue(LC75Arrays().can_place_flowers([1,0,0,0,1], 1))
    self.assertTrue(LC75Arrays().can_place_flowers([1,0,0,0,1,0,0], 0))
    self.assertFalse(LC75Arrays().can_place_flowers([1,0,0,0,1], 2))
    self.assertFalse(LC75Arrays().can_place_flowers([1,0,0,0,0,1], 2))


if __name__ == "__main__":
    unittest.main()
