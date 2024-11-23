# LEETCODE PROBLEM 3 : LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

class Solution(object):
    # BRUTE FORCE APPROACH
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestStringLength = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(list(s[i : j]))) == j - i:
                    longestStringLength = j - i if longestStringLength < j - i else longestStringLength
        return longestStringLength


solution = Solution()
print(solution.lengthOfLongestSubstring('pwwkew'))
