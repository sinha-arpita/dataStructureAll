
# from doubly_linked_list.doubly_linked_list import *
import doubly_linked_list.doubly_linked_list as dll

class LRUCache:

    """
        10  : "Arpita"
        20  : "Arjun"
        30  : "Alokk"
        40  : "Aishani"

        Hash table:
         h[10] = n1
         h[20] = n2
         h[30] = n3
         h[40] = n4

        Linked List
         head-> n1 <-> n2 <-> n3 <-> n4 <- tail

        n1 {
          value : "Arpita",
          key : 10,
          next : n2,
          prev : None
        }
        n2 {
          key : 20,
          value : "Arjun",
          next : n3,
          prev : n1
        }
        n3 {
          key : 30,
          value : "Alokk",
          next : n4,
          prev : n2
        }
        n4 {
          key : 40
          value : "Aishani",
          next : None,
          prev : n3
        }

    """
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.hash = {}
        self.dll = dll.DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.hash:
            return None

        print("VALUE : ", self.dll.printList())
        self.dll.move_to_front(self.hash[key])
        return self.hash[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        node = None

        if key in self.hash:
            node = self.hash[key]
            # this check is only valid when we are inserting new element

        # if we are inserting new node and have hit the limit, evict LRU node
        if  node==None:
            if len(self.hash) == self.limit:
                self.dll.remove_from_tail()
        else:
            # this is existing node, overwrite, and move to front
            node.delete()
        self.hash[key] = self.dll.add_to_head(value)  # override



