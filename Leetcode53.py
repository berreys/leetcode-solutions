# LEETCODE PROBLEM 53 : MAXIMUM SUBARRAY
# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        right = left = 0
        max_sum = min(nums)
        current_sum = nums[0]
        while right < len(nums):
            current_sum += nums[right]
            while current_sum < 0:
                current_sum -= nums[left]
                left += 1
            max_sum = max(max_sum, current_sum)
            right += 1
        return max_sum
        
        
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([5,4,-1,7,8]))