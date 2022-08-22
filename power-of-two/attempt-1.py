class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n == 1:
                return True
            if n%2 !=0:
                return False
            n=n/2
        return False
"""
RESULTS:
1108 / 1108 test cases passed.
Status: Accepted
Runtime: 32 ms
Memory Usage: 13.4 MB
"""