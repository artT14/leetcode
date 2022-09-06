# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         int maxsum=nums[0];
#         int cursum=nums[0];
#         for(int i=1; i<nums.size();++i){
#             cursum= max(cursum+nums[i], nums[i]); //by this we are eleminating sum whenever it becomes negative
#             maxsum= max(cursum, maxsum);
#         }
#         return maxsum;
#     }
# };

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = CURR = nums[0]
        for i in range(1,len(nums)):
            CURR = max(CURR+nums[i],nums[i])
            MAX = max(CURR,MAX)
        return MAX
    
"""
Success
Details 
Runtime: 696 ms, faster than 74.30% of Python online submissions for Maximum Subarray.
Memory Usage: 25.8 MB, less than 23.81% of Python online submissions for Maximum Subarray.
"""