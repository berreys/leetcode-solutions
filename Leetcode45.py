# LEETCODE PROBLEM 45 : JUMP GAME II
# https://leetcode.com/problems/jump-game-ii/description/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #jump and go to wherever would end up with the biggest battery to use, keep doing this until you get to the end
        ptr = 0
        jumps = 0
        while ptr < len(nums) - 1:
            if ptr + nums[ptr] >= len(nums) - 1:
                return jumps + 1
            max = 0
            nextPtr = 0
            for i in range(ptr, ptr + nums[ptr] + 1):
                if i >= len(nums):
                    continue
                if nums[i] + i > max:
                    max = nums[i] + i
                    nextPtr = i
            jumps += 1
            ptr = nextPtr
        return jumps

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))
print(s.jump([1,1,1,1,1]))
print(s.jump([1,1,2,1,1]))
