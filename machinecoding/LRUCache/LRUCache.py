import threading
from entities.DoublyLinkedList import DLL
from entities.Node import Node
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.lst = DLL()    
        self.capacity = capacity
        self._lock = threading.Lock()

    def get(self, key):
        with self._lock:
            if key not in self.cache:
                return None
            node = self.cache[key]
            self.lst.move_to_first(node)
            return node.val
        
    def put(self, key, val):
        print(f"Adding: {key}:{val} to cache")
        with self._lock:
            if key in self.cache:
                node = self.cache[key]
                node.val = val
                self.lst.move_to_first(node)
            else:
                if len(self.cache) == self.capacity:
                    lru = self.lst.remove_last()
                    if lru:
                        del self.cache[lru.key]
                node = Node(key, val)
                self.lst.add_first(node)
                self.cache[key] = node
        print(f"Added: {key}:{val} to cache")

    def print_cache(self):
        for key, val in self.cache.items():
            if key is not None:
                print(f"Key:{key}, Val: {val.val}")