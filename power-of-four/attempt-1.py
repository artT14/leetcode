class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n % 4 != 0 or n < 1:
            return False
        else:
            return self.isPowerOfFour(n/4)
"""
RESULTS:
Runtime: 27 ms, faster than 61.58% of Python online submissions for Power of Four.
Memory Usage: 13.3 MB, less than 66.91% of Python online submissions for Power of Four.
"""