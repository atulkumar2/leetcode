"""Leetcode 75
https://leetcode.com/studyplan/leetcode-75/

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