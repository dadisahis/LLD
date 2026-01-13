from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, order):
        pass

class FlatRateShipping(Strategy):
    def __init__(self, rate: float):
        self.rate = rate
        
    def execute(self, order):
        print(f"Calculating flat rate shipping: {self.rate}")
        return self.rate

class WeightBasedShipping(Strategy):
    def __init__(self, rate_per_kg: float):
        self.rate_per_kg = rate_per_kg

    def execute(self, order):
        cost = order.weight * self.rate_per_kg
        print(f"Calculating weight based shipping: {order.weight}kg * {self.rate_per_kg} = {cost}")
        return cost
    
class DistanceBasedShipping(Strategy):
    def __init__(self, rate_per_km: float):
        self.rate_per_km = rate_per_km

    def execute(self, order):
        cost  = order.dist * self.rate_per_km
        print(f"Calculating distance based shipping: {order.dist}km * {self.rate_per_km} = {cost}")
        return cost
    
class ShippingCostService:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate_shipping(self, order):
        return self.strategy.execute(order)


