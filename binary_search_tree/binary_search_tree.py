import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BinarySearchTree(value)
        root= self
        while True:
           if root.value >new_node.value:
               if root.left is None:
                  root.left=new_node
                  return
               else:
                  root=root.left
           else:
               if root.right is None:
                  root.right=new_node
                  return
               else:
                  root=root.right
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):#target is as values
        root= self
        while True:

           if root.value ==target:
              return True
           if root.value>target:#look on left side
                 if root.left ==None:
                    return False #value is less than root but not on left side
                 else:
                     root=root.left
           else:
                 if root.right==None:
                     return False
                 else:
                     root=root.right
    # Return the maximum value found in the tree
    def get_max(self): # we can get the max value in the rightmost node
        root= self
        while root:
            if root.right ==None:
                return root.value
            else:
                root=root.right





    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # preorder
        root = self

        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal left,root,right
    def in_order_print(self, node):
        root= node
        # print("in_order_print")
        if root:
            # First recur on left child
            self.in_order_print(root.left)

            # then print the data of node
            print(root.value)

            # now recur on right child
            self.in_order_print(root.right)


            # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = deque([node])

        #
        #    1
        #       8
        #    5
        # 3     7
        #2   4  6
        #
        while q:
            node = q.pop()
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
            print(node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if node.left:
            self.dft_print(node.left)
        if node.right:
            self.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT root,left,right
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT left,right,root
    def post_order_dft(self, node):

        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
