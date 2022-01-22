class Listnode:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    def insert(self,node):
        temp=self.head
        if temp==None:
            self.head=node
        else:
            while temp!=None:
                temp=temp.next
            temp.next=node

    
first=Listnode(10)  # none
second=Listnode(20)
third=Listnode(30)

llist=Linkedlist()
llist.head=first


first.next=second
second.next=third

new_node=Listnode(40)
llist.insert(new_node)

