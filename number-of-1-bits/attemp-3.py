class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return format(n,"b").count("1")
"""
RESULTS:
Runtime: 16 ms, faster than 92.94% of Python online submissions for Number of 1 Bits.
Memory Usage: 13.6 MB, less than 10.52% of Python online submissions for Number of 1 Bits.
"""