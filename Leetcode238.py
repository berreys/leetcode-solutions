# LEETCODE PROBLEM 238 : PRODUCT OF ARRAY EXCEPT SELF
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelfSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for i in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    answer[i] *= nums[j]
        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))