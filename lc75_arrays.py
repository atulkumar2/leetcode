"""Leetcode 75

"""

class LC75Arrays:
  """Leetcode easy solutions
  """
  def merge_alternately(self, word1: str, word2: str) -> str:
    """Merge the strings by adding letters in alternating order, starting with word1.
    If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.
    https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

    Args:
        word1 (str): length between 1 and 100
        word2 (str): length between 1 and 100

    Returns:
        str: Merged string
    """
    op = ""
    if len(word1) <= len(word2):
      for i in range(len(word1)):
        op += (word1[i] + word2[i])
      if len(word1) < len(word2):
        op += word2[-(len(word2)-len(word1)):]
    else:
      for i in range(len(word2)):
        op += (word1[i] + word2[i])
      op += word1[-(len(word1)-len(word2)):]

    return op

  def gcd_of_strings(self, str1: str, str2: str) -> str:
    """Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
    "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
    https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

    Args:
        str1 (str): _description_
        str2 (str): _description_

    Returns:
        str: _description_
    """
    strings = [str1, str2]
    if len(str1) > len(str2):
      strings = [str2, str1]

    common = ""
    for i in range(len(strings[0])):
        if common != "" and strings[0][i:].startswith(common): break
        common += strings[0][i]

    common_len = len(common)
    if (common_len == 0) or (len(strings[0]) % common_len) != 0 or (len(strings[1]) % common_len) != 0:
        return ""

    for i in range(len(strings[1]) // common_len):
        if (i*common_len) < len(strings[0]) and not strings[0][i*common_len:].startswith(common):
            return ""
        if not strings[1][i*common_len:].startswith(common):
            return ""

    return common

  def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
    """Return a boolean array result of length n, where result[i] is true if,
    after giving the ith kid all the extraCandies,
    they will have the greatest number of candies among all the kids, or false otherwise.

    Args:
        candies (list[int]): _description_
        extra_candies (int): _description_

    Returns:
        list[bool]: _description_
    """
    max_num = candies[0]
    for candy in candies:
        if candy > max_num:
            max_num = candy

    return [((candy + extra_candies) >= max_num) for candy in candies]
