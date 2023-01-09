"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        result_length = 0
        
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[r] == s[l]: # check odds
                if(r-l+1 > result_length):
                    result = s[l : r+1]
                    result_length = len(result)
                r += 1
                l -= 1
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]: # check evens
                if(r-l+1 > result_length):
                    result = s[l : r+1]
                    result_length = len(result)
                r += 1
                l -= 1
        return result