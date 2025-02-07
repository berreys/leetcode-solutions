# LEETCODE PROBLEM 80 : REMOVE DUPLICATES FROM SORTED ARRAY II 
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] == nums[left]:
                remove_ptr = right + 1
                while remove_ptr < len(nums) and nums[remove_ptr] == nums[left]:
                    nums.pop(remove_ptr)
                right += 2
                left += 2
            else:
                right += 1
                left += 1
        return len(nums)
    
s = Solution()
l = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(l))
print(l)