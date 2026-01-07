from abc import ABC, abstractmethod


# Component Interface
class FileSystemComponent(ABC):
    
    @abstractmethod
    def get_size(self) -> int:
        pass
    
    @abstractmethod
    def print_structure(self, indent: str = "") -> None:
        pass
    
    @abstractmethod
    def delete(self) -> None:
        pass

# Leaf Component
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
    def print_structure(self, indent: str = "") -> None:
        print(f"{indent}File: {self.name} (Size: {self.size} bytes)")

    def delete(self) -> None:
        print(f"Deleting file: {self.name}")

#  Composite Component
class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []
    
    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)
    
    def get_size(self) -> int:
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def print_structure(self, indent: str = "") -> None:
        print(f"{indent}{self.name}/ (Total Size: {self.get_size()} bytes)")
        for child in self.children:
            child.print_structure(indent + "  ")

    def delete(self) -> None:
        for child in self.children:
            child.delete()
        self.children.clear()
        print(f"Deleting folder: {self.name} and its contents")


