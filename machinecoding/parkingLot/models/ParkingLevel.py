from .Vehicle import Vehicle, VehicleType
from .ParkingSpotManager import ParkingSpotManager
from .ParkingSpot import ParkingSpot
from typing import Dict
class ParkingLevel:
    def __init__(self, level_number: int, managers: Dict[VehicleType, ParkingSpotManager]):
        self.level_number = level_number
        self.managers = managers

    def hasAvailableSpot(self, type: VehicleType):
        return self.managers[type].has_available_spot() if type in self.managers else False
    def park(self, type: VehicleType):
        if type not in self.managers:
            raise Exception("Invalid vehicle type")
        return self.managers[type].park()

    def unPark(self, type:VehicleType, spot: ParkingSpot):
        if type not in self.managers:
            raise Exception("Invalid vehicle type")
        return self.managers[type].unPark(spot) 