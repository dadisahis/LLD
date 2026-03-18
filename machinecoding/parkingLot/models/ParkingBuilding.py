from typing import List
from .ParkingLevel import ParkingLevel
class ParkingBuilding:
    def __init__(self, levels: List[ParkingLevel]):
        self.levels = levels

    def allocate(self, vehicle):
        pass
    def release(self, ticket):
        pass