import sys
sys.path.append('../doubly_linked_list')
#from doubly_linked_list import DoublyLinkedList
class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.head=None
        self.tail=None

    def push(self, value):
        new_node=Node(value)
        self.size +=1
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=None
            self.head=new_node

    def pop(self):
        self.size -=1
        if self.head is None:
            return None
        elif self.head.next is None:
            value= self.head.value
            self.head=None
        else:
          value=self.head.value
          self.head=self.head.next
          self.head.prev=None
        return value

    def len(self):
        current= self.head
        count=0
        if self.head is None:
            return 0
        while current is not None:
            count += 1
            current=current.next
        return count