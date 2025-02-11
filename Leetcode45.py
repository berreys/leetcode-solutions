# LEETCODE PROBLEM 45 : JUMP GAME II
# https://leetcode.com/problems/jump-game-ii/description/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #jump and go to wherever would end up with the biggest battery to use, keep doing this until you get to the end