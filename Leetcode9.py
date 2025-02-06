# LEETCODE PROBLEM 9 : PALINDROME NUMBER
# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        stack = []
        while x > 0:
            stack.append(x%10)
            x = int(x/10)
        while len(stack) > 1:
            front = stack.pop(0)
            back = stack.pop()
            if front != back:
                return False
        return True

s = Solution()
print(s.isPalindrome(-10))
print(s.isPalindrome(101))
print(s.isPalindrome(1001))
print(s.isPalindrome(105601))
