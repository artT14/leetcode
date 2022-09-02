class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        low = buy = prices[0]
        profit = sell - buy
        for i in range(1,len(prices)):
            # KEEP TRACK OF LOW
            if prices[i] < low:
                low = prices[i]
            new_prof = max(prices[i] - buy, prices[i] - low)
            # SELL NOW
            if new_prof > profit:
                profit = new_prof
        return max(0,profit)

"""
Success
Details 
Runtime: 1319 ms, faster than 43.26% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 22.6 MB, less than 74.69% of Python online submissions for Best Time to Buy and Sell Stock.
"""