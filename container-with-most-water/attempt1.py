"""
Container With Most Water - https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = height[-1]
        right_idx = len(height) - 1
        left = height[0]
        left_idx = 0
        max = 0
        for i in range(len(height)-1):
            print(i,right_idx)
            diff = right_idx - i
            curr = diff * min(height[i],right)
            if curr > max or (curr == max and height[i] > left): 
                max = curr
                left_idx = i
                left = height[i]
            print(max)            
        for i in reversed(range(left_idx+1,len(height)-1)):
            print(left_idx,i)
            right = height[i]
            diff = i - left_idx
            curr = diff * min(left,right)
            if curr > max: 
                max = curr
            print(max)            
        return max
    
s = Solution()
print(
    s.maxArea([2,3,4,5,18,17,6])
)

# WRONG ANSWER