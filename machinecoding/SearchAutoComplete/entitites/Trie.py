from .Suggestion import Suggestion

class TrieNode:
    def __init__(self):
        self.arr = [None]*26
        self.endWord = False
        self.freq = 0


    def contains_key(self, chr):
        return self.arr[ord(chr)-ord('a')] != None
    
    def get_char(self, chr):
        return self.arr[ord(chr)-ord('a')]
    def insert_char(self, chr, nd):
        self.arr[ord(chr)-ord('a')] = nd
    def set_end(self):
        self.endWord = True
        return
    def get_end(self):
        return self.endWord
    def get_frequency(self):
        return self.freq
    
    def inc_freq(self):
        self.freq +=1
        return
    


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_wrd(self, word):
        curr =  self.root
        for char in word:
            if not curr.contains_key(char):
                curr.insert_char(char, TrieNode())
            curr = curr.get_char(char)
        curr.set_end()
        curr.inc_freq()

    def search_prefix(self, prefix):
        curr = self.root
        for char in prefix:
            if not curr.contains_key(char):
                return None
            curr = curr.get_char(char)
        return curr
    
    def collect_suggestions(self, start_nd, prefix):
        sugg = []
        self._collect(start_nd, prefix, sugg)
        return sugg
    
    def _collect(self, node, prefix, suggestions):
        if node.get_end():
            suggestions.append(Suggestion(prefix, node.get_frequency()))
        for i in range(len(node.arr)):
            if node.arr[i]:
                self._collect(node.arr[i], prefix + chr(97+i),suggestions)
