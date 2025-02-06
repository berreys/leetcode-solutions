# LEETCODE PROBLEM 11 : CONTAINER WITH MOST WATER
# https://leetcode.com/problems/container-with-most-water/description/

class Solution(object):
    def maxAreaSlow(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        map = {}
        for i in range(len(height)):
            for j in range(i, len(height)):
                map[(i, j)] = min(height[i], height[j]) * (j - i)
        max_tuple = (0,0)
        max_capacity = 0
        for i in map:
            if map[i] > max_capacity:
                max_tuple = i
                max_capacity = map[i]
        return max_capacity
    def maxArea(self, height):
        left_ptr = 0
        right_ptr = len(height) - 1
        max_capacity = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
        while left_ptr < right_ptr:
            current_capacity = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            if current_capacity > max_capacity:
                max_capacity = current_capacity
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_capacity

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))