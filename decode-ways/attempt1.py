class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        if s[0] != "0": return 0
        if len(s) == 1: return 1
        dp[0] = 1
        dp[1] = 2
        decodable = [str(x) for x in range(1,27)]
        for i in range(1,len(s)):
            if s[i:i+2] in decodable and '0' not in s[i:i+2]:
                dp[i] += dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[len(s)-1]
        # 188/269 PASSED, NOT ACCEPTED