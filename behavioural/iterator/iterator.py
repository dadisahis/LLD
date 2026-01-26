from abc import ABC, abstractmethod

# Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abstractmethod
    def next(self):
        pass


# Iterable Collection Interface
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self)-> Iterator:
        pass

# Concrete Collection
class Playlist(IterableCollection):
    def __init__(self):
        self.songs = []

    def add_song(self, song: str):
        self.songs.append(song)

    def get_song_at(self, ind: int) -> str:
        return self.songs[ind]
    
    def get_size(self)-> int:
        return len(self.songs)
    
    def create_iterator(self):
        return PlaylistIterator(self)

# Concrete Iterator 
class PlaylistIterator(Iterator):
    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.current_ind = 0
    
    def has_next(self)-> bool:
        return self.current_ind < self.playlist.get_size()
    
    def next(self):
        song = self.playlist.get_song_at(self.current_ind)
        self.current_ind += 1
        return song