# LEETCODE PROBLEM 274 : H-INDEX
# https://leetcode.com/problems/h-index/description/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        myMap = {}
        for i in citations:
            myMap[i] = 0
        print(myMap)
        for i in range(len(citations)):
            for j in range(1, citations[i] + 1):
                if j in myMap:
                    myMap[j] += 1                
        print(myMap)
        max = 1
        for key in myMap:
            if myMap[key] >= key and key > max:
                max = key
        return max
    
s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([1,3,1]))
print(s.hIndex([100]))