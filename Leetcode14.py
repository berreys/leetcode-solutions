# LEETCODE PROBLEM 14 :  LONGEST COMMON PREFIX
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0]
        for s in strs:
            if len(s) < len(result):
                result = s
        for i in range(0, len(strs)):
            for j in range(len(strs[i])):
                if j >= len(result):
                    break
                if strs[i][j] != result[j]:
                    result = result[:j]
        return result
    
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))     # "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))        # ""
print(solution.longestCommonPrefix(["ab", "a"]))                    # "a"
print(solution.longestCommonPrefix(["","b"]))                       # ""
print(solution.longestCommonPrefix(["reflower","flow","flight"]))   # ""