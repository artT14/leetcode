class Solution(object):
    def maxProfit(self, prices):
        i = 0
        low, high, maxProfit = 100000000000, 0, 0
        for currentVal in prices:
            if currentVal <= low:
                low = currentVal
            # high is set and current val is greater than high
            elif currentVal - low > maxProfit:
                maxProfit = currentVal - low
        return maxProfit

"""
Success
Details 
Runtime: 1151 ms, faster than 62.00% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 22.2 MB, less than 97.75% of Python online submissions for Best Time to Buy and Sell Stock.
"""