# LEETCODE PROBLEM 15 : 3SUM
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        endPtr = result
        while list1 or list2:
            if list1 and list2:
                endPtr.next = list1 if list1.val < list2.val else list2
                endPtr = endPtr.next
                if list1.val < list2.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
            elif list1:
                endPtr.next = list1
                return result.next
            elif list2:
                endPtr.next = list2
                return result.next
        return result.next

solution = Solution()
node14 = ListNode(val=4)
node12 = ListNode(val=2, next=node14)
node11 = ListNode(val=1, next=node12)
node24 = ListNode(val=4)
node23 = ListNode(val=3, next=node24)
node21 = ListNode(val=1, next=node23)
def printList(ll):
    while ll:
        print(ll.val, end=" ")
        ll = ll.next
printList(solution.mergeTwoLists(node11, node21))