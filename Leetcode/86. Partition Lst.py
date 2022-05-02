# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x) :
        l1=ListNode()
        l2=ListNode()
        temp1=l1
        temp2=l2
        if not head : 
            return 
        
        while head:
            if head.val<x:
                temp1.next=head
                temp1=temp1.next
                
            else:
                temp2.next=head
                temp2=temp2.next
                
            head=head.next
            
            
        temp1.next=l2.next
        temp2.next=None
        
        return l1.next