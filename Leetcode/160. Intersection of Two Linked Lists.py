# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :
        
        def getlength(head):
            
            temp = head
            l = 0
            while temp:
                temp = temp.next
                l += 1
            return l
        
        def traverse(head,l):
            for i in range(l):
                head = head.next
            return head
            
        l1 = getlength(headA)
        l2 = getlength(headB)
        
        if l2 > l1 :
            headB = traverse(headB,l2-l1)
        elif l1 > l2:
            headA = traverse(headA,l1-l2)
            
            
        ptr1 = headA
        ptr2 = headB
       
        
        while ptr1 != ptr2 and (ptr1 and ptr2)  :
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1