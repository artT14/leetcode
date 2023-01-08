class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BASED ON house-robber
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]), nums[-1])
        # run algo of house-robber by taking off either first or last element to prevent adjacency
    def helper(self,nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2