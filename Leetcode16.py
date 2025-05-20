# LEETCODE PROBLEM 16 : THREE SUM CLOSEST
# https://leetcode.com/problems/3sum-closest/description/

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #NESTED FOR LOOP APPROACH
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if abs(target - closest) > abs(target - nums[i] - nums[j] - nums[k]):
                        closest = nums[i] + nums[j] + nums[k]
        return closest

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
