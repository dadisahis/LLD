from .PieceType import PieceType


class Player:
    def __init__(self,name:str, peice: PieceType):
        self.name = name
        self.peice = peice

    def get_name(self):
        return self.name

    def get_peice(self):
        return self.peice
    
    def set_name(self, name):
        self.name = name

    def set_peice(self, peice):
        self.peice = peice