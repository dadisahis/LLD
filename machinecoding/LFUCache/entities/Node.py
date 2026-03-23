class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = self.prev = None
        