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
    
            
ll=LinkedList()
ll.insert_at_end(7)
ll.insert_at_end(6)
ll.print_list()
        
        
