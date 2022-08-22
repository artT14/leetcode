class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1: return False
        while (n % 2 == 0): n /= 2
        return n == 1
"""
RESULTS:
Runtime: 22 ms, faster than 85.67% of Python online submissions for Power of Two.
Memory Usage: 13.3 MB, less than 62.55% of Python online submissions for Power of Two.
"""