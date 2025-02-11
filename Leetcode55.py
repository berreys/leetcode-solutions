# LEETCODE PROBLEM 55 : JUMP GAME
# https://leetcode.com/problems/jump-game/description/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        battery = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            if battery == 0 and nums[i] == 0:
                return False
            battery = max(battery, nums[i])
            battery -= 1

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))