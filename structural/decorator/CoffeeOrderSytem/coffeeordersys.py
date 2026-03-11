from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def get_description(self) -> str:
        return "Simple Coffee"

    def cost(self) -> float:
        return 2.0
    

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
       self.coffee = coffee


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_description(self):
        return self.coffee.get_description() + ", Milk"

    def cost(self):
        return self.coffee.cost() + 0.5
    
class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_description(self):
        return self.coffee.get_description() + ", Sugar"

    def cost(self):
        return self.coffee.cost() + 0.2
    

class WhippedCreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_description(self):
        return self.coffee.get_description() + ", Whipped Cream"

    def cost(self):
        return self.coffee.cost() + 0.7
    

if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(coffee.get_description())  # Output: Simple Coffee
    print(coffee.cost())             # Output: 2.0

    coffee_with_milk = MilkDecorator(coffee)
    print(coffee_with_milk.get_description())  # Output: Simple Coffee, Milk
    print(coffee_with_milk.cost())             # Output: 2.5

    coffee_with_sugar = SugarDecorator(coffee_with_milk)
    print(coffee_with_sugar.get_description())  # Output: Simple Coffee, Milk, Sugar
    print(coffee_with_sugar.cost())             # Output: 2.7

    coffee_with_whipped_cream = WhippedCreamDecorator(coffee_with_sugar)
    print(coffee_with_whipped_cream.get_description())  # Output: Simple Coffee, Milk, Sugar, Whipped Cream
    print(coffee_with_whipped_cream.cost())             # Output: 3.4