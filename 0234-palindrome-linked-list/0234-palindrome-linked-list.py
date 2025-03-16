# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        
        temp = head
        copy = self.copyList(head)

        rev  = self.reverseList(copy)

        while temp and rev:

            if temp.val != rev.val :

                return False
            
            else:
                temp = temp.next
                rev = rev.next

        return True


    def reverseList(self, head):

        if head is not None :       
            prev = None
            curr = head
            temp = head.next

            while curr:

                curr.next = prev
                prev = curr 
                curr = temp 
                if temp != None:
                    temp = temp.next 
                else:
                    temp = None
            return prev
        
        else:
            return head
        
    def copyList(self, head):

        if not head:
            return None
        
        new_head = ListNode(head.val)
        new_curr = new_head
        old_curr = head.next

        while old_curr:
            new_node = ListNode(old_curr.val)
            new_curr.next = new_node
            new_curr = new_node
            old_curr = old_curr.next
        
        return new_head