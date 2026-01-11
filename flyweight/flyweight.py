from abc import ABC, abstractmethod
from typing import Dict, Tuple

# Flyweight Interface 
class Character(ABC):
    @abstractmethod
    def draw(self, x: int, y: int) -> None:
        pass

# Concrete Flyweight
class ConcreteCharacter(Character):
    def __init__(self, char: str, font_size: str, font_family: str, color:str) -> None:
        self.char = char
        self.font_size = font_size
        self.font_family = font_family
        self.color = color

    def draw(self, x: int, y: int) -> None:
        print(f"Drawing character '{self.char}' at ({x}, {y}) with font size '{self.font_size}', font family '{self.font_family}', color '{self.color}'")



# Flyweight Factory
class CharacterFactory:
    def __init__(self) -> None:
        self._characters: Dict[Tuple[str, str, str, str], Character] = {}

    def get_character(self, char: str, font_size: str, font_family: str, color:str) -> Character:
        key = (char, font_size, font_family, color)
        if key not in self._characters:
            self._characters[key] = ConcreteCharacter(char, font_size, font_family, color)
        return self._characters[key]

    def get_character_count(self) -> int:
        return len(self._characters)


# Client Code
class TextEditorClient:
    def __init__(self):
        self.factory = CharacterFactory()
        self.document = []
    
    def add_character(self, char: str, font_size: str, font_family: str, color:str, x: int, y: int) -> None:
        glyph = self.factory.get_character(char, font_size, font_family, color)
        self.document.append(RenderedCharacter(glyph, x, y))

    def render_document(self) -> None:
        for rc in self.document:
            rc.render()
        print(f"Total unique character objects: {self.factory.get_character_count()}")

class RenderedCharacter:
    def __init__(self, glyph: Character, x: int, y: int) -> None:
        self.glyph = glyph
        self.x = x
        self.y = y

    def render(self) -> None:
        self.glyph.draw(self.x, self.y)

