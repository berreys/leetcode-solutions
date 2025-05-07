# LEETCODE PROBLEM 34 : FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target and first == -1:
                first = i
            if nums[i] == target and (i == len(nums) - 1 or nums[i+1] != target):
                last = i
        return [first, last]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 10))
print(solution.searchRange([], 0))
print(solution.searchRange([5,7,7,8,8,10], 5))
print(solution.searchRange([5,5,5,5,5,5,5,5,5,5], 5))