# LEETCODE PROBLEM 121 : BEST TIME TO BUY AND SELL STOCK
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfitSlow(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > maxProfit:
                    maxProfit = diff
        return maxProfit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))