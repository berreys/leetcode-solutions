class Solution(object):
    def maxArea(self, height):
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

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))