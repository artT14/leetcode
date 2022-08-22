class Solution(object):
    def isPowerOfFour(self, n):
        while n:
            if n == 1:
                return True
            if n%4 !=0:
                return False
            n=n/4
        return False
"""
RESULTS:
Runtime: 22 ms, faster than 80.33% of Python online submissions for Power of Four.
Memory Usage: 13.4 MB, less than 66.91% of Python online submissions for Power of Four.
"""