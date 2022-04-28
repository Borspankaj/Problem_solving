# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        l = 1
        temp = head
        
        while temp.next:
            temp = temp.next
            l += 1
        
        if n == l:
            head = head.next
            return head
        val = l-n-1
        temp = head
        while  val > 0:
            temp = temp.next
            val -= 1
         
        temp.next = temp.next.next
        
        return head