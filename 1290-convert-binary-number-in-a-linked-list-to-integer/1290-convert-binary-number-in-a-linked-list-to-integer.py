# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def binary_to_decimal(self,binary):
        return int(binary, 2)
    
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        binary = ''

        curr = head
        while curr:
            binary += str(curr.val)
            curr = curr.next   

        return self.binary_to_decimal(binary)

    