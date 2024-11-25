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
    
    # FASTER APPROACH
    def lengthOfLongestSubstringFaster(self, s):
        longestStringLength = 0
        uniqueChars = set()
        left = 0
        for right in range(len(s)):
            while s[right] in uniqueChars:
                uniqueChars.remove(s[left])
                left += 1
            uniqueChars.add(s[right])
            longestStringLength = len(uniqueChars) if len(uniqueChars) > longestStringLength else longestStringLength
        return longestStringLength

solution = Solution()
print(solution.lengthOfLongestSubstringFast('bbbebbbb'))
