class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        
        l = 0 # left pointer
        maxf = 0 # count of the character with most frequency in the current window
        for r in range(len(s)): #keep moving right pointer
            count[s[r]] = 1 + count.get(s[r],0) # Keep track of number of element
            maxf = max(maxf,count[s[r]]) # if the count of this element is higher than current maxfreq
            
            # windowlen - maxfreq exceeds given k,can;t update any more characters
            if (r - l +1) - maxf > k:
                count[s[l]] -= 1 #decrease count since moving left pointer
                l += 1  # move left pointer
            
            res = max(res, r - l + 1) # if better on this run, update result
        return res