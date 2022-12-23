"""
https://leetcode.com/problems/coin-change/
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1) #default amount
        dp[0] = 0
        
        for a in range(1,amount + 1):
            for coin in coins:
                if a - coin >=0:
                    dp[a] = min(dp[a],1 + dp[a - coin])
                    # Example: a = 7, coin = 3, dp[7] = 1 + dp[4]
        return dp[amount] if dp[amount] != amount + 1 else -1
        #TIME: O(amount*len(coins))
        #MEMORY: O(amount)