# LEETCODE PROBLEM 15 : 3SUM
# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSumSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        threeSums = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        threeSums.add((temp[0], temp[1], temp[2]))
        result = []
        for tuple in threeSums:
            result.append(list(tuple))
        return result
    def binarySearchForNumber(self, nums, target): # return index
        if len(nums) == 0 or len(nums) == 1 and nums[0] != target:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        middle = nums[int(len(nums) / 2)]
        if target == middle:
            return int(len(nums) / 2)
        if target < middle:
            return self.binarySearchForNumber(nums[: int(len(nums) / 2)], target)
        if target > middle:
            index = self.binarySearchForNumber(nums[int(len(nums) / 2):], target)
            if index == -1:
                return index
            return int(len(nums) / 2) + index
    def threeSum(self, nums):
        # sort the array
        # nested for loop - for each pair of numbers, find the compliment - use binary search to find it

        pass
    
s = Solution()
print(s.threeSumSlow([-1,0,1,2,-1,-4]))

print(s.binarySearchForNumber([1,2,3,4,5], 1))
print(s.binarySearchForNumber([1,2,3,4,5], 2))
print(s.binarySearchForNumber([1,2,3,4,5], 3))
print(s.binarySearchForNumber([1,2,3,4,5], 4))
print(s.binarySearchForNumber([1,2,3,4,5], 5))
print(s.binarySearchForNumber([1,2,3,4,5], 6))
print(s.binarySearchForNumber([1,2,3,4,5], 0))
print(s.binarySearchForNumber([1,2,3,4,5], 1.5))
print(s.binarySearchForNumber([1,2,3,4,5], 2.5))
print(s.binarySearchForNumber([1,2,3,4,5], 3.5))
print(s.binarySearchForNumber([1,2,3,4,5], 4.5))
print(s.binarySearchForNumber([1,2,3,4,5,6], 1))
print(s.binarySearchForNumber([1,2,3,4,5,6], 2))
print(s.binarySearchForNumber([1,2,3,4,5,6], 3))
print(s.binarySearchForNumber([1,2,3,4,5,6], 4))
print(s.binarySearchForNumber([1,2,3,4,5,6], 5))
print(s.binarySearchForNumber([1,2,3,4,5,6], 6))