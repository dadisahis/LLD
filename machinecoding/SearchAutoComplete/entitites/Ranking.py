from abc import ABC, abstractmethod
from .Suggestion import Suggestion
from typing import List

class RankingStrategy(ABC):
    @abstractmethod
    def rank(self, suggestions: List[Suggestion]):
        pass


class Alphabetical(RankingStrategy):
    def rank(self, suggestions: List[Suggestion]):
        return sorted(suggestions, key= lambda x: x.word)
    

class Frequency(RankingStrategy):
    def rank(self, suggestions: List[Suggestion]):
        return sorted(suggestions, key= lambda x: x.freq, reverse=True)