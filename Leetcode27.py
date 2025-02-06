# LEETCODE PROBLEM 27 : REMOVE ELEMENT
# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append('_')
                k -= 1
            else:
                k += 1
                i += 1
        return k

s = Solution()
l = [0,1,2,2,3,0,4,2]
s.removeElement(l, 2)
print(l)
