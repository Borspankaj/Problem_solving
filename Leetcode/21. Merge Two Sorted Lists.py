# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1 , list2) :
        ptr1 = list1
        ptr2 = list2
        llist = ListNode()
        ans = llist
        if not ptr1 and not ptr2:
            return None
        
        while ptr1 or ptr2:
            if ptr1 is None:
                llist.next = ptr2
                break
            elif ptr2 is None :
                llist.next = ptr1
                break
            elif ptr1.val <= ptr2.val:
                llist.next = ptr1
                ptr1 = ptr1.next
                
            elif ptr1.val > ptr2.val:
                llist.next = ptr2
                ptr2 = ptr2.next
                
            llist = llist.next
            
        return ans.next