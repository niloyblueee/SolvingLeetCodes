class Node:
    def __init__(self, x):
        self.val = x  # Change from value to val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1 , list2):
        dummy = Node(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:  # Change value to val
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
