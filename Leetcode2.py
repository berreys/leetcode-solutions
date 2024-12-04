# LEETCODE PROBLEM 2

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printListNode(head):
    s = ""
    while head.next != None:
        s += str(head.val) + ", "
        head = head.next
    return s

class Solution(object):

    def addTwoNumbersRecursive(self, l1, l2, carryTheOneFlag, currentNode):
        if l1 == None or l2 == None:
            return
        # TODO: Check for different length numbers
        sum = l1.val + l2.val
        if carryTheOneFlag:
            sum += 1
        if sum >= 10:
            currentNode.val = sum - 10
            carryTheOneFlag = True
        else:
            currentNode.val = sum
            carryTheOneFlag = False
        # TODO: Check for end of number
        currentNode.next = ListNode()
        self.addTwoNumbersRecursive(l1.next, l2.next, carryTheOneFlag, currentNode.next)


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        self.addTwoNumbersRecursive(l1, l2, False, result)
        return result

        

l = ListNode()
l.val = 2
l.next = ListNode()
l.next.val = 4
l.next.next = ListNode()
l.next.next.val = 3

r = ListNode()
r.val = 5
r.next = ListNode()
r.next.val = 6
r.next.next = ListNode()
r.next.next.val = 4

solution = Solution()
print(printListNode(solution.addTwoNumbers(l, r)))