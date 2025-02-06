# LEETCODE PROBLEM 28 : FIND THE INDEX OF THE FIRST OCCURRENCE IN A STRING
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            needleStartingPoint = True
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    needleStartingPoint = False
                    break
            if needleStartingPoint:
                return i
        return -1
            
s = Solution()
haystack = "sadbutsad"
needle = "dad"
print(s.strStr(haystack, needle))