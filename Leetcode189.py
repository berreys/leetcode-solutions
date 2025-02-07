# LEETCODE PROBLEM 189 : ROTATE ARRAY
# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            self.rotate_once(nums)

    def rotate_once(self, nums):
        last = nums.pop()
        nums.insert(0, last)

s = Solution()
l = [1,2,3,4,5]
s.rotate(l, 2)
print(l)