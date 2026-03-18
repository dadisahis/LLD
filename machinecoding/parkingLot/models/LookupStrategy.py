from abc import ABC, abstractmethod


class ParkingSpotLookupStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, parking_lot):
        pass

class NearestParkingSpotLookupStrategy(ParkingSpotLookupStrategy):
    def find_parking_spot(self, parking_lot):
        # Implement logic to find the nearest parking spot for the given vehicle
        pass

class RandomParkingSpotLookupStrategy(ParkingSpotLookupStrategy):
    def find_parking_spot(self, parking_lot):
        # Implement logic to find a random parking spot for the given vehicle
        pass