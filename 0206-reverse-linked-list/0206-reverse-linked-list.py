
class Solution:
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