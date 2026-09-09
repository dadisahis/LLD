from abc import ABC,abstractmethod
from enums import *
class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm, card_no):
        pass
    
    @abstractmethod
    def enter_pin(self, atm, pin):
        pass

    @abstractmethod
    def select_operation(self, atm, operation):
        pass

    def eject_card(self, atm):
        atm.set_current_card(None)
        atm.change_state(IdleState())


class IdleState(ATMState):
    def insert_card(self, atm, card_no):
        print("Card has been inserted")
        card = atm.get_bank_service().auth_card(card_no)
        if card:
            atm.set_current_card(card)
            atm.change_state(HasCardState())
        else:
            self.eject_card(atm)
class HasCardState(ATMState):
    def enter_pin(self, atm, pin):
        print("Authenticating pin")
        card = atm.get_current_card()
        isAuth = atm.get_bank_service().authenticate(card, pin)

        if not isAuth:
            print("Auth Failed: Incorrect PIN")
            self.eject_card(atm)
        else:
            print("Authenticated Successfully")
            atm.change_state(Authenticated())

class Authenticated(ATMState):
    def select_operation(self, atm, operation, **args):
        if operation == TransactionType.BALANCE_INQUIRY:
            atm.check_balance()
        elif operation == TransactionType.WITHDRAWAL:
            if len(args)==0 or args[0]<=0:
                print("Error: Invalied withdrawal amount")
                return

            amt = args[0]
            acc_bal = atm.get_bank_service().get_balance(atm.get_current_card())
            if amt > acc_bal:
                print("Insufficient Balance")
                return
            print("Processing Withdrawal")
            atm.widthraw_cash(amt)
        elif operation == TransactionType.DEPOSIT:
            if len(args)==0 or args[0]<=0:
                print("Error: Invalied Deposit amount")
                return
            
            amt = args[0]
            print("Processing Deposit")
            atm.deposit_cash(amt)
        else:
            print("Invalid operation")
            return
        
        print("Transaction Complete")
        self.eject_card(atm)