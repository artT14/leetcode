"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            r, l = i, i
            # odd palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1
            # even palindrome
            r, l = i+1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1
        return count
        #ACCEPTED