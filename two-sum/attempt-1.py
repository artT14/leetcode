class Solution(object):
    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1
    def qsort(self,inlist):
        if inlist == []: 
            return []
        else:
            pivot = [inlist[0],0]
            lesser = self.qsort([x for x in inlist[1:] if x[0] < pivot[0]])
            greater = self.qsort([x for x in inlist[1:] if x[0] >= pivot[0]])
            return lesser + [pivot] + greater
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = self.qsort(nums)
        print(nums)
        len_nums = len(nums)
        for i in range(len_nums):
            second_target = target - nums[i]
            j = self.binary_search(nums,i+1,len_nums-1,second_target)
            print(i,j)
            if j > -1:
                return [i,j]

sol = Solution()
print(sol.twoSum([3,2,4],6))
"""
RESULTS: wrong
"""