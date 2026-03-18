import threading
from .ParkingSpot import ParkingSpot
from .LookupStrategy import ParkingSpotLookupStrategy
from typing import List

class ParkingSpotManager:
    _lock = None

    def __init__(self, parking_spots: List[ParkingSpot], strategy:ParkingSpotLookupStrategy):
        self.parking_spots = parking_spots
        self.strategy = strategy
        self._lock = threading.Lock()
    
    def has_available_spot(self):
        with self._lock:
            return self.strategy.find_parking_spot(self) is not None
    def park(self):
        with self._lock:
            spot = self.strategy.find_parking_spot(self)
            if spot:
                spot.occupy_spot()
                return spot
            return None
    def unPark(self, spot):
        with self._lock:
            spot.free_spot()



class TwoWheelerSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots, strategy):
        self.parking_spots = parking_spots
        self.strategy = strategy
        super().__init__(parking_spots, strategy)


class FourWheelerSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots, strategy):
        self.parking_spots = parking_spots
        self.strategy = strategy
        super().__init__(parking_spots, strategy)