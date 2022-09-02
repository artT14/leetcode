class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currentMax = 0
        buy = prices[0]
        sell = prices[0]
        
        for price in prices:
            
            if price < buy:
                buy = price
                sell = price
            
            if price > sell:
                sell = price
            
            if sell-buy > currentMax:
                currentMax = sell-buy
                
        
        return currentMax
"""
Success
Details 
Runtime: 1013 ms, faster than 74.34% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 22.7 MB, less than 53.65% of Python online submissions for Best Time to Buy and Sell Stock.
"""