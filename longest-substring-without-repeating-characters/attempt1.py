class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        curr = []
        for c in s:
            if c in curr:
                out = max(len(curr),out)
                i = curr.index(c)
                curr = curr[i+1:]
            curr.append(c)
        out = max(len(curr),out)
        return out
    # ACCEPTED