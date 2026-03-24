from entitites.Trie import *
from entitites.Ranking import *
class AutoComplete:
    def __init__(self, strategy: RankingStrategy, max_res):
        self.trie = Trie()
        self.strategy = strategy
        self.max_res = max_res

    def add_word(self, word):
        self.trie.insert_wrd(word)

    def add_words(self, word_lst):
        for wrd in word_lst:
            self.add_word(wrd)
    
    def get_suggestions(self, prefix):
        pref_nd = self.trie.search_prefix(prefix)
        if pref_nd is None:
            return []
        raw_suggestion = self.trie.collect_suggestions(pref_nd, prefix.lower())
        print(raw_suggestion)
        ranked_sugg = self.strategy.rank(raw_suggestion)

        return [s.word for s in ranked_sugg[:self.max_res]]

        