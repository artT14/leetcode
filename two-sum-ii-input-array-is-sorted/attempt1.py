class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(l,r,target):
            m = (l + r) // 2
            while r >= l:
                m = (l + r) // 2
                if numbers[m] == target:
                    return m
                elif numbers[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return None
        for i in range(len(numbers)):
            n = numbers[i]
            local_target = target - n
            j = binSearch(i+1,len(numbers)-1,local_target)
            if j: return [i+1,j+1]
        # ACCEPTED