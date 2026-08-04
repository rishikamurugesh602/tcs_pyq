class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,val):
        new_node=Node(val)
      
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
    def print_list(self):
        temp=self.head
        if self.head is None:
            return None
    
        while temp is not None:
            if temp.next is not None:
                print(temp.data,end="->")
            else:
                print(temp.data,end="->None")
            temp=temp.next
    def reverse_list(self):
        prev=None
       
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
            
ll=LinkedList()
ll.insert_at_end(7)
ll.insert_at_end(6)
ll.print_list()
print()
print(ll.middle())
        
        
