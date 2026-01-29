from state import *

def main():
    vm = VendingMachine()
    vm.insert_money(5)
    vm.select_item("Soda")
    vm.insert_money(2)
    vm.dispense_item()


    vm.select_item("Soda")
    vm.insert_money(2)
    vm.dispense_item()

if __name__ == "__main__":
    main()