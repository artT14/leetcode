class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {len(s): 1}
        DECODABLE = [str(x) for x in range(1,27)]
        for i in range(len(s)-1,-1,-1): #BOTTOM UP DP
            if s[i] == "0": #0 is not a valid encoding
                dp[i] = 0 # set to 0, no valid encodings
            else: 
                dp[i] = dp[i + 1] # copy last position's value
            if i + 1 < len(s) and s[i:i+2] in DECODABLE:
                dp[i] += dp[i+2] # similiar approach to fibonacci
        return dp[0]