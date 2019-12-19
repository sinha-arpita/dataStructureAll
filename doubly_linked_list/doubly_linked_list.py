"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length


    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length+=1
        if not self.head and not self.tail:
            self.head= new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head= new_node

    def remove_from_head(self):
        self.length -= 1
        if self.head is None:
           return None
        elif self.head is self.tail:
           old_head_value = self.head.value
           self.head = None
           self.tail= None

        else:
           old_head_value=self.head.value
           self.head= self.head.next
           self.head.prev= None
        return old_head_value

    def add_to_tail(self, value):
        new_node= ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
           self.head=new_node
           self.tail=new_node
        else:
          new_node.prev= self.tail
          self.tail.next= new_node
          self.tail=new_node
          new_node.next=None



    def remove_from_tail(self):
        self.length -=1
        if self.tail is None:
          return None
        elif self.head is self.tail:
          val = self.head.value
          self.head=None
          self.tail=None
        else:
          val = self.tail.value
          self.tail=self.tail.prev
          self.tail.next=None

        return val

   #Removes the input node from its current spot in the List and inserts it as the new head node of the List
    def move_to_front(self, node):
        if not self.head:
          return None

        elif node is self.head:
          return
        elif node is self.tail:
          self.tail= node.prev
          node.prev.next=None

        # make surrounding nodes point to each other
        prev_node= node.prev
        next_node= node.next

        if prev_node:
            prev_node.next=next_node
        if next_node:
            next_node.prev= prev_node

        # make it the new head
        node.next=self.head
        self.head.prev=node
        self.head=node

      # Removes the input node from its current spot in the List and inserts it as the new tail node of the List

    def move_to_end(self, node):
        if self.head is None:
          return
        elif node is self.tail:
          return

        elif node is self.head:
         self.head = node.next
         self.head.prev=None

        # make surrounding nodes point to each other
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        # make it the new tail
        node.prev=self.tail
        self.tail.next= node
        self.tail=node
        node.next=None

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
          self.head = None
          self.tail = None
        elif node is self.head:
          self.head = self.head.next
          self.head.prev = None
        elif node is self.tail:
          self.tail = self.tail.prev
          self.tail.next = None
        else:
          node.prev.next = node.next
          node.next.prev = node.prev


    def get_max(self):
        if self.head is None:
          return None
        max_val = self.head.value
        current = self.head
        while current:
          if current.value > max_val:
            max_val = current.value
          current = current.next
        return max_val



