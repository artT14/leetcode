from heapq import heapify, heappush, heappop

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap,num)
        last = heappop(heap)
        count = [1]
        while heap:
            curr = heappop(heap)
            if curr == last+1:
                count[-1] += 1
            elif curr == last:
                continue
            else:
                count.append(1)
            last=curr
        return max(count)
        # ACCEPTED