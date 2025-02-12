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
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for _ in nums]
        pre = [i for i in nums]
        post = [i for i in nums]
        for i in range(1, len(nums)):
            pre[i] *= pre[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] *= post[i + 1]
        for i in range(len(nums)):
            if i == 0:
                answer[i] = post[i + 1]
            elif i == len(nums) - 1:
                answer[i] = pre[i - 1]
            else:
                answer[i] = post[i + 1] * pre[i - 1]
        return answer



s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))