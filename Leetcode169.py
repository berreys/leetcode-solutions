# LEETCODE PROBLEM 169 : MAJORITY ELEMENT
# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        num_to_beat = int(len(nums) / 2)
        myMap = {}
        for i in range(len(nums)):
            if nums[i] in myMap:
                myMap[nums[i]] += 1
                if myMap[nums[i]] > num_to_beat:
                    return nums[i]
            else:
                myMap[nums[i]] = 1