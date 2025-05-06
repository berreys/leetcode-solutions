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

    def getPalindrome(self, s1, s2, vertex):
        si1 = len(s1) - 1
        si2 = 0
        while s1[si1] == s2[si2]:
            si1 -= 1
            si2 += 1
            if si1 == -1 or si2 >= len(s2):
                break
        return s1[si1 + 1:] + vertex + s2[:si2]

    def longestPalindromeFaster(self, s):
        if len(s) < 2 or (len(s) == 2 and s[0] == s[1]):
            return s
        longest = s[0]
        for i in range(1, len(s)):
            temp = ''
            if i < len(s) - 1 and s[i-1] == s[i+1]:
                temp = self.getPalindrome(s[:i], s[i+1:], s[i])
            if s[i-1] == s[i]:
                temp1 = self.getPalindrome(s[:i], s[i:], '')
                temp = temp1 if len(temp1) > len(temp) else temp
            longest = temp if len(temp) > len(longest) else longest
        return longest


solution = Solution()
print(solution.longestPalindromeFaster('cbbd'))     # bb
print(solution.longestPalindromeFaster('babad'))    # bab
print(solution.longestPalindromeFaster('a'))        # a
print(solution.longestPalindromeFaster('ab'))       # a
print(solution.longestPalindromeFaster('abc'))      # a
print(solution.longestPalindromeFaster('abcdefgh')) # a
print(solution.longestPalindromeFaster('bb'))       # bb
print(solution.longestPalindromeFaster('ccc'))      # ccc
print(solution.longestPalindromeFaster('abb'))      # bb
print(solution.longestPalindromeFaster('aaaa'))     # aaaa