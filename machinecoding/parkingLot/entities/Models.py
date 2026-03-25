import uuid
from datetime import datetime
from .enums import VehicleType
import math
class ParkingSpot:
    def __init__(self, spot_id,vehicle_type, rate_per_hour):
        self.spot_id=spot_id
        self.vehicle_type = vehicle_type
        self.rate_per_hour = rate_per_hour
        self.occupied_by = None
    
    def is_availble(self):
        return self.occupied_by == None
    def occupy(self, vehicle):
        self.occupied_by = vehicle
        return
    def remove(self):
        self.occupied_by = None
        return

class Vehicle:
    def __init__(self, id, type):
        self.id = id
        self.type = type


class Ticket:
    def __init__(self, vehicle, spot):
        self.id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.start_time = datetime.now()

    def calculate_bill(self):
        exhasuted_time = datetime.now() - self.start_time
        hour = exhasuted_time.total_seconds() / 3600
        billed_hour = 1  if hour ==0 else math.ceil(hour)
        return billed_hour * self.spot.rate_per_hour 
    

class Floor:
    def __init__(self, id):
        self.id = id
        self.mp = {
            VehicleType.BIKE : [],
            VehicleType.TRUCK: [],
            VehicleType.CAR: []
        }
    def add_spot(self, spot: ParkingSpot):
        self.mp[spot.vehicle_type].append(spot)
    def find_available_spot(self, type: VehicleType):
        spots = self.mp[type]
        for spot in spots:
            if spot.is_availble():
                return spot
        return None
    
class ParkingLot:
    def __init__(self):
        self.floors = []

    def add_floor(self, floor: Floor):
        self.floors.append(floor)
        return
    
