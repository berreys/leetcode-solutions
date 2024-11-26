# LEETCODE PROBLEM 4 : MEDIAN OF TWO SORTED ARRAYS

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1index, nums2index = 0, 0
        combinedList = []
        while nums1index < len(nums1) and nums2index < len(nums2):
            if nums1[nums1index] < nums2[nums2index]:
                combinedList.append(nums1[nums1index])
                nums1index += 1
            else:
                combinedList.append(nums2[nums1index])
                nums1index += 1
        print(combinedList)

    def findMedianSortedArraysFaster(self, nums1, nums2):
        # find middle of each list, compare
        # on larger number, find middle of left side of list, reverse for smaller number
        # TODO: Draw this out
        #note: keep track of left side and right side. when you partition, higher number right side goes up, lower number left side goes up
        return

solution = Solution()
print(solution.findMedianSortedArrays([1,2,3,4], [1,2,3,4]))