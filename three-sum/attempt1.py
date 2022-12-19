"""
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        accumulator = []
        for x in nums:
            for i in range(len(accumulator)):
                z = accumulator[i] + [x]
                if len(z) == 3:
                    if (z[0] + z[1] + z[2] == 0):
                        z.sort()
                        if z not in answer:
                            answer.append(z)
                else: accumulator.append(z)
            accumulator.append([x])
        return answer
    
s = Solution()
print(
    s.threeSum([-1,0,1,2,-1])
)

#RESULT: time limit exceeded