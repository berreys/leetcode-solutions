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
        nums = list(set(nums))
        nums.sort()
        results = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                compliment_index = self.binarySearchForNumber(nums, 0 - nums[i] - nums[j])
                if compliment_index != -1 and compliment_index != i != j:
                    results.append([nums[i], nums[j], nums[compliment_index]])
        return results
    def twoSumHelper(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i
    def twoSum(self, nums, target):
        temp = self.twoSumHelper(nums, target)
        if temp:
            return [nums[temp[0]], nums[temp[1]]]
    def threeSumFaster(self, nums):
        results = set()
        for i in range(len(nums)):
            temp = self.twoSum(nums[:i] + nums[i+1:], -1 * nums[i])
            if temp:
                temp.append(nums[i])
                results.add(tuple(sorted(temp)))
        return [list(i) for i in results]
            
    

    
s = Solution()
print(s.threeSumFaster([-1,0,1,2,-1,-4]))
print(s.threeSumFaster([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# print(s.binarySearchForNumber([1,2,3,4,5], 1))
# print(s.binarySearchForNumber([1,2,3,4,5], 2))
# print(s.binarySearchForNumber([1,2,3,4,5], 3))
# print(s.binarySearchForNumber([1,2,3,4,5], 4))
# print(s.binarySearchForNumber([1,2,3,4,5], 5))
# print(s.binarySearchForNumber([1,2,3,4,5], 6))
# print(s.binarySearchForNumber([1,2,3,4,5], 0))
# print(s.binarySearchForNumber([1,2,3,4,5], 1.5))
# print(s.binarySearchForNumber([1,2,3,4,5], 2.5))
# print(s.binarySearchForNumber([1,2,3,4,5], 3.5))
# print(s.binarySearchForNumber([1,2,3,4,5], 4.5))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 1))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 2))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 3))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 4))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 5))
# print(s.binarySearchForNumber([1,2,3,4,5,6], 6))