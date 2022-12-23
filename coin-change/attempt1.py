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
        remainder = amount
        coins = 0
        coins.sort(reverse=True)
        while remainder > 0 and len(coins):
            for coin in coins:
                if remainder - coin >= 0:
                    remainder -= coin
                    num_coins += 1
                    break
                else:
                    coins = coins[1:]
        if remainder != 0:
            num_coins = -1
        return num_coins

#RESULT: wrong solution
