from abc import ABC, abstractmethod

from .Vehicle import Vehicle


class ParkingSpot:
    def __init__ (self, spotId: str, isFree:bool):
        self.spotId = spotId
        self.isFree = isFree
    def get_spot_id(self):
        return self.spotId
    def is_free(self):
        return self.isFree
    def occupy_spot(self):
        self.isFree = False
    def free_spot(self):
        self.isFree = True


# class TwoWheelerSpot(ParkingSpot):
#     def __init__(self, id: str, price: float, is_occupied: bool, vehicle: Vehicle):
#         super().__init__(id, price, is_occupied, vehicle)
#     def return_price(self):
#         return self.price

# class FourWheelerSpot(ParkingSpot):
#     def __init__(self, id: str, price: float, is_occupied: bool, vehicle: Vehicle):
#         super().__init__(id, price, is_occupied, vehicle)
#     def return_price(self):
#         return self.price