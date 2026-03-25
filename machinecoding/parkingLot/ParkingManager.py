from entities.Models import *
class ParkingManager:
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot
        self.tickets = {}

    def park_vehicle(self,vehicle: Vehicle):
        spot = None
        for floor in self.parking_lot.floors:
            spot = floor.find_available_spot(vehicle.type)
            if spot:
                spot.occupy(vehicle)
                ticket = Ticket(vehicle, spot)
                self.tickets[ticket.id] = ticket
                print(f"Vehicle {vehicle.id} occupies {spot.spot_id}")
                return ticket.id
        print("No spots available")
        return None
    
    def unpark_vehicle(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            amount  = ticket.calculate_bill()
            ticket.spot.remove()
            del self.tickets[ticket_id]
            print(f"Vehicle {ticket.vehicle.id} has to pay ${amount}")
            return amount
        print("Ticket is invalid")
        return None