from abc import ABC, abstractmethod
from .enum import Piece

# Parent
class PieceType:
    def __init__(self, piece: Piece):
        self.piece = piece

#Child: PieceX, PieceO - Is A relationship
class PieceX(PieceType):
    def __init__(self):
        super().__init__(Piece.X)
    def __str__(self):
        return self.piece.value

class PieceO(PieceType):
    def __init__(self):
        super().__init__(Piece.O)

    def __str__(self):
        return self.piece.value