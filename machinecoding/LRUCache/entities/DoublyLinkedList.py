from .Node import Node
class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next , self.tail.prev = self.tail, self.head

    def add_first(self, node:Node):
        node.next = self.head.next
        node.prev = self.head.prev
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node):
        prev, nxt= node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def move_to_first(self, node: Node):
        self.remove(node)
        self.add_first(node)

    def remove_last(self):
        if self.tail.prev == self.head:
            return None 
        last = self.tail.prev
        self.remove(last)
        return last
