from entities.DLL import DLL
from entities.Node import Node
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_mp ={}
        self.freq_mp ={}
        self.minFreq = 0

    def update(self, node):
        freq = node.freq
        self.freq_mp[freq].remove(node)
        if freq == self.minFreq  and self.freq_mp[freq].size ==0:
            self.minFreq +=1
        freq+=1
        node.freq = freq
        if freq not in self.freq_mp:
            self.freq_mp[freq] = DLL()
        self.freq_mp[freq].insert(node)

    def get(self, key):
        if key not in self.key_mp:
            return -1
        node = self.key_mp[key]
        self.update(node)
        return node.val
    
    def put(self, key, val):
        if self.capacity == 0:
            return
        if key in self.key_mp:
            node = self.key_mp[key]
            node.val = val
            self.update(node)
        else:
            if len(self.key_mp) == self.capacity:
                lfu_list = self.freq_mp[self.minFreq]
                lru = lfu_list.pop_left()
                del self.key_mp[lru.key]
            node = Node(key, val)
            self.key_mp[key] = node
            self.minFreq = 1
            if 1 not in self.freq_mp:
                self.freq_mp[1] = DLL()
            self.freq_mp[1].insert(node)
        
        
    def print_cache(self):
        if len(self.key_mp)>0:
            for key, val in self.key_mp.items():
                print(f"Key={key}, val={val.val}, freq={val.freq}")
        return