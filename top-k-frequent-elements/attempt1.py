class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        sorted_hm = sorted(hm.items(), key=lambda item: item[1], reverse=True)
        out = []
        for i in range(k):
            out.append(sorted_hm[i][0])
        return out
        # ACCEPTED