# LEETCODE PROBLEM 5 : LONGEST PALINDROMIC SUBSTRING
# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def isPalindrome(self, s):
        myStack = []
        for i in range(0, int(len(s)/2)):
            myStack.append(s[i])
        for i in range(int(len(s)/2) if len(s) % 2 == 0 else int(len(s)/2) + 1, len(s)):
            if s[i] == myStack.pop():
                if len(myStack) == 0:
                    return True
            else:
                return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 0
        if len(s) == 1:
            return s
        longest = s[0]
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                temp = s[i:j]
                if self.isPalindrome(s[i:j]):
                    longest = longest if len(longest) > j - i else s[i:j]
        return longest

solution = Solution()
print(solution.longestPalindrome('cbbd'))