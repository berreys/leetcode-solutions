# LEETCODE PROBLEM 7 : REVERSE INTEGER
# https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = x < 0
        if isNegative:
            x *= -1
        newNum = 0
        while x > 0:
            newNum *= 10
            newNum += x % 10
            x = int(x / 10)
        if newNum > 2**31 - 1:
            return 0
        return newNum if not isNegative else -1 * newNum


solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(210))
print(solution.reverse(1534236469))