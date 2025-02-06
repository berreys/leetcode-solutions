# LEETCODE PROBLEM 15 : 3SUM
# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSumSlow(self, nums):
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
    def threeSum(self, nums):
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        set1 = {}
        for i in range(len(nums)):
            set2 = {}
            for j in range(i+1, len(nums)):
                
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))