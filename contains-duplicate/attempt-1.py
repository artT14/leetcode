class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = True
            else:
                return True
        return False

"""
Success
Details 
Runtime: 403 ms, faster than 85.60% of Python online submissions for Contains Duplicate.
Memory Usage: 24 MB, less than 41.31% of Python online submissions for Contains Duplicate.
"""