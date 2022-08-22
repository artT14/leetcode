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
            n = n / 2
        return c
"""
RESULTS:
Runtime: 23 ms, faster than 74.72% of Python online submissions for Number of 1 Bits.
Memory Usage: 13.3 MB, less than 86.33% of Python online submissions for Number of 1 Bits.
"""