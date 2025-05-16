# LEETCODE PROBLEM 6 : ZIGZAG CONVERSION
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        arr = [["" for i in range(len(s))] for j in range(numRows)]
        count = 0
        down = True
        currLocation = [0,0]
        while count < len(s):
            if currLocation[0] < 0:
                currLocation[0] += 2
                currLocation[1] -= 1
                down = True
            if currLocation[0] >= numRows:
                currLocation[0] -= 2
                currLocation[1] += 1
                down = False
            arr[currLocation[0]][currLocation[1]] = s[count]
            count += 1
            if down:
                currLocation[0] += 1
            else:
                currLocation[0] -= 1
                currLocation[1] += 1
        result = ""
        for i in arr:
            for j in i:
                result += j
        return result
        

solution = Solution()
print(solution.convert("ABC", 1))