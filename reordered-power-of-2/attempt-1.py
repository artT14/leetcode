class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_d = list(format(n,"d"))
        n_d.sort(reverse=True)
        max = int(''.join(n_d))
        counter = 1
        while(counter <= max):
            # CHECK CONDITION
            ctr_d = list(format(counter,"d"))
            ctr_d.sort(reverse=True)
            if n_d == ctr_d:
                return True
            counter *= 2
        return False


s = Solution()

print(
    s.reorderedPowerOf2(46)
)

"""
Success
Details 
Runtime: 26 ms, faster than 89.47% of Python online submissions for Reordered Power of 2.
Memory Usage: 13.4 MB, less than 68.42% of Python online submissions for Reordered Power of 2.
"""