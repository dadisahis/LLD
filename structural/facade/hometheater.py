from abc import ABC, abstractmethod


class Amplifier:
    def on(self):
        print("Amplifier is on")

    def off(self):
        print("Amplifier is off")

    def set_volume(self, level):
        print(f"Amplifier volume set to {level}")

class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def off(self):
        print("DVD Player is off")

    def play(self, movie):
        print(f"Playing movie: {movie}")
    def stop(self):
        print("DVD Player stopped")


class Projector:
    def on(self):
        print("Projector is on")

    def off(self):
        print("Projector is off")

    def set_input(self, source):
        print(f"Projector input set to {source}")

class SmartLights:
    def on(self):
        print("Smart Lights are on")

    def off(self):
        print("Smart Lights are off")

    def set_color(self, color):
        print(f"Smart Lights color set to {color}")

class StreamingService:
    def connect(self):
        print("Connected to streaming service")

    def disconnect(self):
        print("Disconnected from streaming service")

    def play_content(self, content):
        print(f"Playing content: {content}")


class HomeTheaterFacade:
    def __init__(self):
        self.amplifier = Amplifier()
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.smart_lights = SmartLights()
        self.streaming_service = StreamingService()
    
    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.smart_lights.on()
        self.smart_lights.set_color("dimmed")
        self.projector.on()
        self.projector.set_input("DVD Player")
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)
    def end_movie(self):
        print("Shutting down movie theater...")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.projector.off()
        self.amplifier.off()
        self.smart_lights.off()

if __name__ == "__main__":
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("Inception")
    home_theater.end_movie()