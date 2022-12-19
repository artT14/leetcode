"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort() # sort the list first
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: continue # skip duplicates
            hm = set() # hashmap
            for j, num2 in enumerate(nums[i+1:]):
                if -num-num2 in hm:
                    if j+i+2 < len(nums) and num2 == nums[j+i+2]: continue # skip duplicates
                    triplets = [num, -num-num2, num2]
                    result.append(triplets)
                else:
                    hm.add(num2)
        return result
    
s = Solution()
print(
    s.threeSum([-1,0,1,2,-1])
)

# RESULT: accepted