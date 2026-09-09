import threading
class ATM:
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        if not self._init:
            self.state = IdleState()
            self.bank_service =  BankService()

            self.cash_dispenser = CashDispenser()

    def set_state(self, state):
        self.state = state
    def insert_card(self, card):
        self.state.insert_card(card)
    def enter_pin(self.)