
from entities.Models import *
from ParkingManager import ParkingManager
def main():
    lot = ParkingLot()

    floor = Floor(1)
    floor.add_spot(ParkingSpot(1, VehicleType.CAR, 10))
    floor.add_spot(ParkingSpot(2, VehicleType.BIKE, 5))
    lot.add_floor(floor)

    service = ParkingManager(lot)
    
    ticket_id = service.park_vehicle(Vehicle("DL9C123", VehicleType.CAR))

    if ticket_id:
        service.unpark_vehicle(ticket_id)


if __name__ == '__main__':
    main()

