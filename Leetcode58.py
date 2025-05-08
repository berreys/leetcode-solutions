# LEETCODE PROBLEM 58 : LENGTH OF LAST WORD
# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])

solution = Solution()
print(solution.lengthOfLastWord("hello there bro"))