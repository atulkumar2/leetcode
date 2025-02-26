"""Leetcode 75
https://leetcode.com/studyplan/leetcode-75/

"""

class LC75EasyTwoPointers:
    """https://leetcode.com/studyplan/leetcode-75/
    """
    def move_zeroes(self, nums: list[int]) -> None:
        """
        Move all 0's to the end of nums while maintaining the relative order of the non-zero elements.

        Do this in-place without making a copy of the array.
        Do not return anything, modify nums in-place instead.
        https://leetcode.com/problems/move-zeroes/
        """
        next_replacement = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if next_replacement == -1:
                    next_replacement = i
                continue

            if next_replacement != -1:
                nums[next_replacement] = nums[i]
                nums[i] = 0
                next_replacement += 1

        if next_replacement != -1:
            for i in range(next_replacement, len(nums)):
                nums[i] = 0

    def is_subsequence(self, s: str, t: str) -> bool:
        """Check if s is a subsequence of t, or false otherwise.

          A subsequence of a string is a new string that is formed from the original string by deleting some
          (can be none) of the characters without disturbing the relative positions of the remaining characters.
          (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

          https://leetcode.com/problems/is-subsequence/

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        if 0 == len(s) + len(t):
            return True
        if 0 == len(t):
            return False
        if 0 == len(s):
            return True

        last_find = -1
        for i in range(len(s)):
            if last_find == (len(t) - 1):
                return False
            try:
                if last_find == -1:
                    last_find = t.index(s[i], 0)
                else:
                    last_find = t.index(s[i], last_find+1)
            except:
                return False

        return (last_find != -1)

class LC75EasyArrays:
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
        if str1[0] != str2[0]:
            return ""
        if str1 == str2:
            return str1

        strings = [str1, str2]
        if len(str1) > len(str2):
            strings = [str2, str1]
        strlens = [len(strings[0]), len(strings[1])]

        checkpoint = 0
        common = strings[0][0]
        for i in range(1, strlens[0]):
            if strings[0][i] != strings[1][i]:
                break
            common += strings[0][i]
            if strlens[0] % (i+1) == 0 and strlens[1] % (i+1) == 0:
                checkpoint = i
        if checkpoint != len(common):
            common = strings[0][:checkpoint+1]

        common_len = len(common)
        for i in range(strlens[1] // common_len):
            if (i*common_len) < strlens[0] and not strings[0][i*common_len:].startswith(common):
                return ""
            if not strings[1][i*common_len:].startswith(common):
                return ""

        return common

    def kids_with_candies(self, candies: list[int], extra_candies: int) -> list[bool]:
        """Return a boolean array result of length n, where result[i] is true if,
        after giving the ith kid all the extraCandies,
        they will have the greatest number of candies among all the kids, or false otherwise.
        https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

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

    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        """A long flowerbed. Some of the plots are planted, and some are not.
        Flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
        and an integer n, return true if n new flowers can be planted in the flowerbed
        without violating the no-adjacent-flowers rule and false otherwise.
        https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

        Args:
            flowerbed (list[int]): _description_
            n (int): _description_

        Returns:
            bool: _description_
        """
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            return False

        if (flowerbed[0] + flowerbed[1]) == 0:
            n -= 1
            flowerbed[0] = 1
            if n == 0:
                return True

        for i in range(1, len(flowerbed) - 1):
            if (flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]) == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        if (flowerbed[-2] + flowerbed[-1]) == 0:
            n -= 1
            flowerbed[-1] = 1

        return n == 0

    def reverse_vowels(self, s: str) -> str:
        """Given a string s, reverse only all the vowels in the string and return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

        https://leetcode.com/problems/reverse-vowels-of-a-string/

        Args:
            s (str): _description_

        Returns:
            str: _description_
        """
        vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pos_v = []
        for i in range(len(s)):
            if s[i] in vowels:
                pos_v.append(i)

        s = list(s)
        for i in range(round(len(pos_v)/2)):
            temp = s[pos_v[i]]
            s[pos_v[i]] = s[pos_v[-(i+1)]]
            s[pos_v[-(i+1)]] = temp

        return "".join(s)

class LC75MediumArrays:
    """Leetcode medium solutions
    """
    def reverse_words(self, s: str) -> str:
        """Given an input string s, reverse the order of the words.
        The words in s will be separated by at least one space.
        Return a string of the words in reverse order concatenated by a single space.
        https://leetcode.com/problems/reverse-words-in-a-string/


        Args:
            s (str): _description_

        Returns:
            str: _description_
        """
        parts = s.split()
        parts.reverse()
        return " ".join([part for part in parts])

    def product_except_self(self, nums: list[int]) -> list[int]:
        """Return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        Algorithm must run in O(n) time and without using the division operation.

        https://leetcode.com/problems/product-of-array-except-self/

        Args:
            nums (list[int]): _description_

        Returns:
            list[int]: _description_
        """

        if len(nums) == 2:
            return [nums[1],nums[0]]

        answer = [1]
        mult = 1
        for i in range(1, len(nums)):
            mult = (mult * nums[i-1])
            answer.append(mult)

        mult = 1
        for j in range(len(nums)-2, -1, -1):
            mult = (mult * nums[j+1])
            answer[j] = (answer[j] * mult)

        return answer

class LC75EasyPrefixSum:
    """LG75 Prefix sum problems
    """
    def largest_altitude(self, gain: list[int]) -> int:
        """There is a biker going on a road trip.
        The road trip consists of n + 1 points at different altitudes.
        The biker starts his trip on point 0 with altitude equal 0.

        You are given an integer array gain of length n where gain[i] is
        the net gain in altitude between points i​​​​​​ and i + 1 for all
        (0 <= i < n). Return the highest altitude of a point.

        https://leetcode.com/problems/find-the-highest-altitude/

        Args:
            gain (list[int]): _description_

        Returns:
            int: _description_
        """
        high_alt = 0
        last_alt = 0

        for gain_t in gain:
            last_alt = last_alt + gain_t
            if last_alt > high_alt:
                high_alt = last_alt

        return high_alt

    def pivot_index(self, nums: list[int]) -> int:
        """Calculate the pivot index of nums.

        The pivot index - sum of all numbers strictly to left of index is equal to sum of all numbers strictly to index's right.

        If index is on left edge of the array, then the left sum is 0.
        This also applies to the right edge of the array.

        Return the leftmost pivot index. If no such index exists, return -1.
        https://leetcode.com/problems/find-pivot-index/


        Args:
            nums (list[int]): _description_

        Returns:
            int: _description_
        """

        if len(nums) == 1:
            return 0

        sum_l = 0
        sum_r = 0
        for i in range(1, len(nums)):
            sum_r += nums[i]

        for i in range(len(nums)):
            if i != 0:
                sum_l += nums[i-1]
                sum_r -= nums[i]

            if sum_l == sum_r:
                return i

        return -1


class LC75EasyHashMapSet:
    """LC75 Easy Hashmap and Set problems
    """
    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """Given two integer arrays nums1 and nums2.
        Return a list answer of size 2 where:
            answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
            answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

        Integers in the lists may be returned in any order.

        https://leetcode.com/problems/find-the-difference-of-two-arrays/

        Args:
            nums1 (list[int]): _description_
            nums2 (list[int]): _description_

        Returns:
            list[list[int]]: _description_
        """
        res = [[],[]]

        if nums1[0] not in nums2:
            res[0].append(nums1[0])
        if nums2[0] not in nums1:
            res[1].append(nums2[0])

        nums2 = set(nums2)
        nums1 = set(nums1)
        for num in nums1:
            if (num not in nums2) and (num not in res[0]):
                res[0].append(num)

        for num in nums2:
            if (num not in nums1) and (num not in res[1]):
                res[1].append(num)

        return res
