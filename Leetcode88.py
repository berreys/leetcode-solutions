# LEETCODE PROBLEM 88 : MERGE SORTED ARRAY
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        nums1_ptr = 0
        nums2_ptr = 0
        while nums1_ptr + nums2_ptr < m + n:
            if nums2_ptr == n:
                return
            if nums1_ptr == m:
                for i in range(nums1_ptr + nums2_ptr, len(nums1)):
                    self.insert(nums1, nums2[nums2_ptr], i)
                    nums2_ptr += 1
                return
            if nums1[nums1_ptr + nums2_ptr] > nums2[nums2_ptr]:
                self.insert(nums1, nums2[nums2_ptr], nums1_ptr + nums2_ptr)
                nums2_ptr += 1
            else:
                nums1_ptr += 1

    def insert(self, nums_list, num, index):
        for i in range(len(nums_list)-1, index, -1):
            nums_list[i] = nums_list[i-1]
        nums_list[index] = num

s = Solution()
l1 = [2,0]
l2 = [1]
print(l1)
s.merge(l1, 1, l2, 1)
print(l1)

l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
print(l1)
s.merge(l1, 3, l2, 3)
print(l1)
