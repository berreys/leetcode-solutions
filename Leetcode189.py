# LEETCODE PROBLEM 189 : ROTATE ARRAY
# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        right = nums[len(nums) - k:len(nums)]
        left = nums[0:len(nums) - k]
        nums[:] = right + left

s = Solution()
l = [1,2,3,4,5]
s.rotate(l, 2)
print(l)