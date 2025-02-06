# LEETCODE PROBLEM 15 : 3SUM
# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        threeSums = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        threeSums.add((temp[0], temp[1], temp[2]))
        result = []
        for tuple in threeSums:
            result.append(list(tuple))
        return result
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))