# LEETCODE PROBLEM 1 : TWO SUM

class Solution(object):
    # NESTED FOR LOOP APPROACH
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()
print(solution.twoSum([3,2,4], 6))