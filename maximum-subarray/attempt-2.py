import functools

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        curr = functools.reduce(lambda a, b: a+b, nums)
        LOW, HIGH, MAX = 0, length - 1, curr
        for i in range(length - 1):
            curr -= nums[i]
            if curr > MAX: LOW, MAX = i, curr
        MAX = curr = functools.reduce(lambda a, b: a+b, nums)
        for i in range(length-1, 0, -1):
            curr -= nums[i]
            if curr > MAX: HIGH, MAX = i,curr
        print(LOW, HIGH)
        return 0 + functools.reduce(lambda a, b: a+b, nums[LOW:HIGH])

sol = Solution()

print(
    sol.maxSubArray(
[-2,1,-3,4,-1,2,1,-5,4])
)

"""
WRONG ANSWER:

"""