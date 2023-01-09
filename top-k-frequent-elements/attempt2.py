# GENIUS O(n) solution by NeetCode
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums: # count using hashmap
            count[n] = 1 + count.get(n,0)
        for n,c in count.items(): #for each frequency, add the corresponding number to list
            freq[c].append[n]
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            # if any items in this frequency, enter the following loop
            for n in freq[i]:
                res.append(n) # guaranteed to be next highest frequency
                if len(res) == k: #time to terminate, we have reached k in output
                    return res