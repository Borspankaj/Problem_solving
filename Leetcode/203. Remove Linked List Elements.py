# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):
        if head == None:
            return head
        
        while head :
            if head.val == val :
                head = head.next
            else:
                break
        if not head:
            return head
        temp = prev = head 
        while  prev.next:
            if temp.val == val :
                if temp.next == None:
                    prev.next = None
                
                else : 
                    prev.next = temp.next
                    temp = prev.next
            else:
                prev = temp
                temp = temp.next
             
        return head