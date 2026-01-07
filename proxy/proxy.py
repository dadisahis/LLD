from abc import ABC, abstractmethod
import time

# Subject Interface
class Image(ABC):
    
    @abstractmethod
    def get_file_name(self) -> str:
        pass
    
    @abstractmethod
    def display(self) -> None:
        pass

# Real Subject
class HighResImage(Image):
    def __init__(self, file_name: str):
        self._file_name = file_name
        self.image_data = None
        self._load_image_from_disk()

    def _load_image_from_disk(self) -> None:
        print(f"Loading high resolution image from disk: {self._file_name}")
        try :
            time.sleep(2)
            self.image_data = bytearray(1024 * 1024 * 5)  # Simulate loading a large image (5MB)
            print(f"Image {self._file_name} loaded successfully.")
        except KeyboardInterrupt:
            print("Loading interrupted.")
    
    def get_file_name(self) -> str:
        return self._file_name
    
    def display(self) -> None:
        print(f"Displaying high resolution image: {self._file_name}")


#Proxy
class ImageProxy(Image):
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._real_image = None

    def get_file_name(self) -> str:
        return self._file_name
    
    def display(self) -> None:
        if self._real_image is None:
            self._real_image = HighResImage(self._file_name)
        else:
           print(f"ImageProxy: Using cached high-resolution image for {self._file_name}")

        self._real_image.display()