from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass

class MP3Player(MediaPlayer):
    def play(self, filename):
        print(f"Playing MP3 file: {filename}")
class VLCCodec:
    def play_vlc(self, filename):
        print(f"Playing VLC file: {filename}")

class MP4Codec:
    def play_mp4(self, filename):
        print(f"Playing MP4 file: {filename}")

class VLCPlayerAdapter(MediaPlayer):
    def __init__(self, codec):
        self.codec = codec

    def play(self, filename):
        self.codec.play_vlc(filename)


class MP4PlayerAdapter(MediaPlayer):
    def __init__(self, codec):
        self.codec = codec

    def play(self, filename):
        self.codec.play_mp4(filename)


class AudioPlayer:
    def play_file(self, filename):
        extension = filename.split('.')[-1].lower()
        players = {
            'mp3': MP3Player(),
            'vlc': VLCPlayerAdapter(VLCCodec()),
            'mp4': MP4PlayerAdapter(MP4Codec())
        }
        player = players.get(extension)
        if player:
            player.play(filename)
        else:
            print(f"Unsupported file format: {extension}")

if __name__ == "__main__":
    audio_player = AudioPlayer()
    audio_player.play_file("song.mp3")
    audio_player.play_file("movie.vlc")
    audio_player.play_file("video.mp4")
    audio_player.play_file("document.pdf")