# LEETCODE PROBLEM 19 : REMOVE NTH NODE FROM END OF LIST
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        arr[-n-1].next = arr[-n+1]
        return head
    
s = Solution()
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

from util import Util
u = Util()
u.printLinkedList(n1)
# u.printLinkedList(Solution().removeNthFromEnd(n1, 2))
u.printLinkedList(Solution().removeNthFromEnd(n5, 1))