# LEETCODE PROBLEM 26 : REMOVE DUPLICATES FROM SORTED ARRAY
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        k = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                k += 1
                i += 1
        return k + 1
    
s = Solution()
l = [1,1,2]
print(s.removeDuplicates(l))
print(l)