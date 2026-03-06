from abc import ABC, abstractmethod

class EnemyPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Enemy(EnemyPrototype):
    def __init__(self, type ,health, attack, speed, weapon, inventory):
        self.type = type
        self.health = health
        self.attack = attack
        self.speed = speed
        self.weapon = weapon
        self.inventory = list(inventory)

    def clone(self):
        return Enemy(self.type, self.health, self.attack, self.speed, self.weapon, list(self.inventory))
    
    def set_health(self, health):
        self.health = health
    
    def add_inventory_item(self, item):
        self.inventory.append(item)

    def print_status(self):
        print(f"Enemy Type: {self.type}, Health: {self.health}, Attack: {self.attack}, Speed: {self.speed}, Weapon: {self.weapon}, Inventory: {self.inventory}")


class EnemyRegistry:
    def __init__(self):
        self._prototypes = {}
    
    def register(self, name, prototype):
        self._prototypes[name] = prototype
    
    def get(self, name):
        prototype = self._prototypes.get(name)
        if prototype is None:
            raise ValueError(f"No prototype registered under name: {name}")
        return prototype.clone()
    
if __name__ == "__main__":
    register = EnemyRegistry()

    goblin_prototype = Enemy("Goblin", 100, 15, 10, "Club", ["Gold Coin"])
    register.register("goblin", goblin_prototype)

    witch_prototype = Enemy("Witch", 150, 25, 8, "Magic Staff", ["Potion"])
    register.register("witch", witch_prototype)

    goblin1 = register.get("goblin")
    goblin2 = register.get("goblin")

    goblin2.set_health(80)
    goblin2.add_inventory_item("Dagger")


    witch1 = register.get("witch")
    goblin1.print_status()
    goblin2.print_status()
    witch1.print_status()