"""
https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # bottom up Dynamic Programming 
        dp = [False] * (len(s) + 1) # initialize all to False, default case
        dp[len(s)] = True # Base case True, if we every get to it, then we are able to use dict to segment string
        for i in range(len(s)-1,-1,-1): #traverse every index in reverse
            for w in wordDict: # at most consider every word
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w: # if within boundaries and there is a word match
                    dp[i] = dp[i + len(w)] # update value based on past cases
                if dp[i]: # if we have a vlaue that's True, no need to consider other words, break loop
                    break
        return dp[0] # dp[0] should give us final answer