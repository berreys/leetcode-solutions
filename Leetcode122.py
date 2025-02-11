# LEETCODE PROBLEM 122 : BEST TIME TO BUY AND SELL STOCK II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        localMin = prices[0]
        goingUp = False
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                goingUp = True
            if goingUp and prices[i] < prices[i-1]:
                goingUp = False
                sum += prices[i-1] - localMin
                localMin = prices[i]
            if goingUp and i == len(prices) - 1:
                sum += prices[i] - localMin
            if prices[i] < localMin:
                localMin = prices[i]
        return sum
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([2,4,1]))