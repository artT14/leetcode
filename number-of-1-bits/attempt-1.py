class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            if n % 2 == 1: 
                c+=1
            n = n >> 1
        return c
"""
RESULTS:
Runtime: 43 ms, faster than 9.76% of Python online submissions for Number of 1 Bits.
Memory Usage: 13.4 MB, less than 62.17% of Python online submissions for Number of 1 Bits.
"""