from .Node import Node
class DLL:
    def __init__(self):
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0


    def insert(self, node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        self.size +=1

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -=1
    
    def pop_left(self):
        if self.size > 0:
            node = self.left.next
            self.remove(node)
            return node
        return None