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
    def maxProfitSlightlyFaster(self, prices):
        myMap = {}
        for i in range(1, len(prices)):
            myMap[i-1] = prices[i] - prices[i-1]
            for elem in myMap:
                if prices[i] - prices[elem] > myMap[elem]:
                    myMap[elem] = prices[i] - prices[elem]
        max = 0
        for elem in myMap:
            if myMap[elem] > max:
                max = myMap[elem]
        return max
    def maxProfit(self, prices):
        low = prices[0]
        max = 0
        for i in prices:
            if i < low:
                low = i
            elif i - low > max:
                max = i - low
        return max



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([2,1,4]))