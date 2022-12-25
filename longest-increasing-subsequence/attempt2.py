"""
https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [1] * len(nums) #CACHE
        
        for i in range(len(nums) - 1, -1, -1): # reverse order
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS) 

        # O(n^2)
        #EXAMPLE RUN:
        """
        [10,9,2,5,3,7,101,18]
        i=7 j=n/a 
            move to next i
        i=6 j=7 
            nums[6] < nums[7] == 101 < 18 NO
        i=6 j=n/a
            move to next i
        i=5 j=6 
            nums[5] < nums[6] == 7 < 101 YES 
            LIS[5]  = max(LIS[5],1+LIS[6])
                    = max(1,2) = 2
            LIS[5] = 2
        i=5 j=7 
            nums[5] < nums[7] == 7 < 18 YES
            LIS[5]  = max(LIS[5],1+LIS[7])
                    = max(2,1+1) = 2
            LIS[5]  = 2
        i=5 j=n/a
            move to next i
        i=4 j=5
            nums[4] < nums[5] == 3 < 7 YES
            LIS[4]  = max(LIS[4],1+LIS[5])
                    = max(1,3)
            LIS[4]  = 3
        i=4 j=6
            nums[4] < nums[6] == 3 < 101 YES
            LIS[4]  = max(LIS[4],1+LIS[6])
                    = max(3,2)
            LIS[4]  = 3
        i=4 j=7
            nums[4] < nums[7] == 3 < 18 YES
            LIS[4]  = max(LIS[4],1+LIS[7])
                    = max(3,2)
            LIS[4]  = 3
        i=4 j=n/a
            move to next i
        i=3 j=4
            nums[3] < nums[4] == 5 < 3 NO
        i=3 j=5
            nums[3] < nums[5] == 5 < 7 YES
            LIS[3]  = max(LIS[3],1+LIS[5])
                    = max(1,3)
            LIS[3]  = 3
        i=3 j=6
            nums[3] < nums[6] == 5 < 101 YES
            LIS[3]  = max(LIS[3],1+LIS[6])
                    = max(3,2)
                    = 3
        i=3 j=7
            nums[3] < nums[7] == 5 < 18 YES
            LIS[3]  = max(LIS[3],1+LIS[7])
                    = max(3,2)
                    = 3
        i=3 j=n/a
            move to next i
        i=2 j=3
            nums[2] < nums[3] == 2 < 5 YES
            LIS[2]  = max(LIS[2],1+LIS[3])
                    = max(1,4)
                    = 4
        ...
        i=2 j=n/a
            move to next i
        i=1 j=2
            nums[1] < nums[2] == 9 < 2 NO
        i=1 j=3
            nums[1] < nums[3] == 9 < 5 NO
        i=1 j=4
            nums[1] < nums[4] == 9 < 3 NO
        i=1 j=5
            nums[1] < nums[5] == 9 < 7 NO
        i=1 j=6
            nums[1] < nums[6] == 9 < 101 YES
            LIS[1]  = max(LIS[1],1+LIS[6])
                    = max(1,2)
                    = 2
        i=1 j=7
            nums[1] < nums[7] == 9 < 18 YES
            LIS[1]  = max(LIS[1],1+LIS[7])
                    = max(2,2)
                    = 2
        i=1 j=n/a
            move to next i
        i=0 j=1
            nums[0] < nums[1] == 10 < 9 NO
        i=0 j=2
            nums[0] < nums[2] == 10 < 2 NO
        ...
        i=0 j=6
            nums[0] < nums[6] == 10 < 101 YES
            LIS[0]  = max(LIS[0],1+LIS[6])
                    = max(1,2)
                    = 2
        i=0 j=7
            nums[0] < nums[7] == 10 < 18 YES
            LIS[0]  = max(LIS[0],1+LIS[7])
                    = max(2,2)
                    = 2
        i=0 j=n/a
            move on to next i
        i=n/a
            FIN
        """