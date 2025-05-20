class Util(object):
    def printLinkedList(self, head):
        s = ""
        while head:
            s += str(head.val) + " "
            head = head.next
        print(s)