from abc import ABC, abstractmethod
import time
class MachineState(ABC):
    @abstractmethod
    def select_item(self, context, item):
        pass
    @abstractmethod
    def insert_money(self, context, amount):
        pass
    @abstractmethod
    def dispense_item(self, context):
        pass

class IdleState(MachineState):
    def select_item(self, context, item_cd):
        print(F"Item {item_cd} selected.")
        context.set_selected_item(item_cd)
        context.set_state(ItemSelectedState())
    def insert_money(self, context, amount):
        print("Please select an item first.")
    def dispense_item(self, context):
        print("No  Item selected. Nothing to dispense.")

class ItemSelectedState(MachineState):
    def select_item(self, context, item):
        print(f"Item already selected: {context.get_selected_item()}.")
    def insert_money(self, context, amount):
        print(F"Inserted ${amount}.")
        context.set_inserted_money(amount)
        context.set_state(HasMoneyState())
    def dispense_item(self, context):
        print("Please insert money first.")

class HasMoneyState(MachineState):
    def select_item(self, context, item):
        print(f"Cannot change after money inserted. Current item: {context.get_selected_item()}.")
    def insert_money(self, context, amount):
        print("Money already inserted.")
    
    def dispense_item(self, context):
        print(F"Dispensing item {context.get_selected_item()}. Enjoy!")
        context.set_state(DispensingState())
        time.sleep(1)
        print("Item dispensed.")
        context.reset()

class DispensingState(MachineState):
    def select_item(self, context, item):
        print("Currently dispensing. Please wait.")
    def insert_money(self, context, amount):
        print("Currently dispensing. Please wait.")
    def dispense_item(self, context):
        print("Already dispensing an item.")


class VendingMachine:
    def __init__(self):
        self.current_state = IdleState()
        self.selected_item = None
        self.inserted_money = 0
    def set_state(self, state):
        self.current_state = state
    def set_selected_item(self, item):
        self.selected_item = item
    
    def get_selected_item(self):
        return self.selected_item
    def set_inserted_money(self, amount):
        self.inserted_money = amount
    def select_item(self, item):
        self.current_state.select_item(self, item)
    def insert_money(self, amount):
        self.current_state.insert_money(self, amount)
    def dispense_item(self):
        self.current_state.dispense_item(self)
    
    def reset(self):
        self.selected_item = None
        self.inserted_money = 0
        self.set_state(IdleState())

        