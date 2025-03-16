# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:

    def MiddleNodeIdx(self,head):

        idx = 0
        curr = head
        while curr:
            idx += 1
            curr = curr.next

        if idx%2 == 0:
            return math.ceil(idx//2)

        else:
            return idx//2

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        idx = self.MiddleNodeIdx(head)
        curr = head
        count = 0
        while curr:
            
            if count == idx :
                head = curr
                break
            
            else:
                curr = curr.next
                count += 1
        return head


