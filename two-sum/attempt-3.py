class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[target-nums[i]] = i
            else:
                return [i, mapping[nums[i]]]
"""
Runtime: 65 ms, faster than 76.95% of Python online submissions for Two Sum.
Memory Usage: 14 MB, less than 97.81% of Python online submissions for Two Sum.
"""

"""
EXAMPLE RUN:
    INPUT: [0,2,5,9,15,33], 24
    0 - Key 0 Not in Mapping, mapping{24: 0} NEXT 
    1 - Key 2 Not in Mapping, mapping{24: 0, 22: 1} NEXT
    2 - Key 5 Not in Mapping, mapping{24: 0, 22: 1, 19: 2} NEXT
    3 - Key 9 Not in Mapping, mapping{24: 0, 22: 1, 19: 2, 15: 3} NEXT
    3 - Key 15 Found in Mapping with value 3, RETURN [4,3]
"""
sol = Solution()
print(sol.twoSum([0,2,5,9,15,33], 24))