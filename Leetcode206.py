# LEETCODE PROBLEM 206 : REVERSE LINKED LIST
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        leftPtr = None
        rightPtr = head
        while rightPtr:
            temp = rightPtr.next
            rightPtr.next = leftPtr
            leftPtr = rightPtr
            rightPtr = temp
        return leftPtr

def printLL(head):
    while head:
        print(head.val)
        head = head.next
    
solution = Solution()
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

printLL(solution.reverseList(None))