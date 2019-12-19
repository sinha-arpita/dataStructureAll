import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.head= None
        self.tail=None

    def enqueue(self, value):

        new_node = Node(value)
        self.size +=1
        # we enque in the last .. so add to the tail
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def dequeue(self):

     if self.head is None:
        return None
     else:
        value= self.head.value
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        self.size -= 1
        return value


    def len(self):

        if self.head is None:
            return 0
        current=self.head
        size = 0
        while current:
          size += 1
          current = current.next
        return size