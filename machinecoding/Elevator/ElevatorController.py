from entities.Elevator import Elevator
from entities.Request import Request
from entities.ElevatorStrategy import *
class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators

    def assign_elevator(self, request: Request):
        best_el = min(self.elevators, key=lambda a: abs(a.current_floor - request.source))
        print(f"Assiging elevator {best_el.id}")
        best_el.add_request(request)

    def step(self):
        for el in self.elevators:
            el.move()


if __name__ == '__main__':
    elevators = [Elevator(id=1,strategy=SimpleStrategy()), Elevator(id=2,strategy=SimpleStrategy(), current_floor=5)]
    controller = ElevatorController(elevators)

    requests = [
        Request(2, 8),
        Request(6, 1),
        Request(3, 7)
    ]

    for req in requests:
        controller.assign_elevator(req)

    for _ in range(5):
        controller.step()