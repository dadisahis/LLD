from iterator import *


def main():
    playlist = Playlist()
    playlist.add_song("1. Beat It")
    playlist.add_song("2. Billie Jean")
    playlist.add_song("3. Thriller")
    playlist.add_song("4. Smooth Criminal")


    iterator = playlist.create_iterator()

    while iterator.has_next():
        song = iterator.next()
        print(f"Playing song: {song}")



if __name__ == '__main__':
    main()