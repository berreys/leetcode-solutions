# LEETCODE PROBLEM 35 : SEARCH INSERT POSITION
# https://leetcode.com/problems/search-insert-position/description/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) > 0 and nums[0] > target:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target and nums[i-1] < target:
                return i
            if i == len(nums) - 1:
                return i + 1
            

solution = Solution()
print(solution.searchInsert([1,3,5,6], 1))
print(solution.searchInsert([1,3,5,6], 3))
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 6))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3], 2))