
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        ans=ListNode()
        result=ans
        s=0
        carry=0
        while l1 or l2:
            if l1 and l2:
                value=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
               
            elif l1 and not l2:
                value=l1.val+carry
                l1=l1.next
                
            else:
                value=l2.val+carry
                l2=l2.next
            s=value%10
            carry=value//10   
            ans.next=ListNode(s)
            ans=ans.next
            
        if carry==1:
            ans.next=ListNode(carry)
            
        return result.next