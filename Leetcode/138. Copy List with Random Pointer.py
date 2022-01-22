
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        hmap={}
        temp=head
        if not temp:
            return head
        while temp:
            hmap[temp]=Node(temp.val)
            temp=temp.next
            
        for node in hmap:
            if node.next==None:
                hmap[node].next=None
            else:
                hmap[node].next=hmap[node.next]
    
            if node.random==None:
                hmap[node].random=None
            else:
                hmap[node].random=hmap[node.random]
            
        return hmap[head]
#---------------------------------------------------------------------------------------
#
#---------------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        temp=head
        if head==None:
            return head
        
        
        while temp:
          
            newnode=Node(temp.val)
            newnode.next=temp.next
            temp.next=newnode
                
            temp=newnode.next
        
        temp=head
        while temp:
            if temp.random==None:
                temp.next.random==None
                
            else:
                temp.next.random=temp.random.next
                
            temp=temp.next.next
                
        
        result=temp2=head.next
        temp1=head
        
        while temp1:
            temp1.next=temp1.next.next
            if temp2.next==None:
                temp2.next=None
            else:
                
                temp2.next=temp2.next.next
            temp1=temp1.next
            temp2=temp2.next
            
        return result