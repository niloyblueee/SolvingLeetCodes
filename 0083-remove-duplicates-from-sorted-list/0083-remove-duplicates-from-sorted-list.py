# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        checker = head
        while checker and checker.next :
            if checker.val == checker.next.val:
                checker.next = checker.next.next

            else:
                checker = checker.next
        return head        







        






























