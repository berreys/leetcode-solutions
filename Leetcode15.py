# LEETCODE PROBLEM 15 : 3SUM
# https://leetcode.com/problems/3sum/description/

cache = {}
cache2 = {}
class Solution(object):
    def twoSumHelper(self, nums, target):
        if str(nums) + " " + str(target) in cache:
            return cache[str(nums) + " " + str(target)]
        results = []
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                results.append([d[target - nums[i]], i])
            else:
                d[nums[i]] = i
        cache[str(nums) + " " + str(target)] = results
        return results
    def twoSum(self, nums, target):
        if str(nums) + " " + str(target) in cache2:
            return cache2[str(nums) + " " + str(target)]
        temp = self.twoSumHelper(nums, target)
        results = []
        for i in range(len(temp)):
            results.append([nums[temp[i][0]], nums[temp[i][1]]])
        cache2[str(nums) + " " + str(target)] = results
        return results
    def threeSumFaster(self, nums):
        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1
        nums = []
        for i in freqs:
            if i == 0 and freqs[i] > 2:
                nums.append(i)
                nums.append(i)
                nums.append(i)
            if freqs[i] > 1:
                nums.append(i)
                nums.append(i)
            else:
                nums.append(i)
        results = set()
        for i in range(len(nums)):
            temp = self.twoSum(nums[:i] + nums[i+1:], -1 * nums[i])
            for j in range(len(temp)):
                results.add(tuple(sorted(temp[j] + [nums[i]])))
        return [list(i) for i in results]
            
    

    
s = Solution()
# print(s.threeSumFaster([-1,0,1,2,-1,-4]))
# print(s.threeSumFaster([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(s.threeSumFaster([0,0,1,1,-1,-1]))
print(s.threeSumFaster([0,0,0]))

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