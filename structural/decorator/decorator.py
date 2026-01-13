"""
Docstring for decorator.decorator
This file implements decorator pattern in system design

"""

from abc import ABC, abstractmethod


# Component Interface
class TextView(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

# Concrete Component
class PlainTextView(TextView):
    def __init__(self, text: str):
        self._text = text

    def display(self) -> str:
        return self._text
    

# Decorator Base Class
class TextViewDecorator(TextView):
    def __init__(self, inner: TextView):
        self._inner = inner

# Concrete Decorators
class BoldDecorator(TextViewDecorator):
    def __init__(self, inner: TextView):
        super().__init__(inner) #calls the constructor of parent class and sets the inner component
    
    def display(self) -> str:
        return f"<b>{self._inner.display()}</b>"
    
class ItalicDecorator(TextViewDecorator):
    def __init__(self, inner: TextView):
        super().__init__(inner)
    
    def display(self) -> str:
        return f"<i>{self._inner.display()}</i>"
    
class UnderlineDecorator(TextViewDecorator):
    def __init__(self, inner: TextView):
        super().__init__(inner)
    
    def display(self) -> str:
        return f"<u>{self._inner.display()}</u>"
    


