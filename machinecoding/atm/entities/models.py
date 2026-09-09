import threading

class Card:
    def __init__(self, number, pin, acc_no):
        self._card_no = number
        self._pin = pin

    @property
    def card_number(self):
        return self._card_no
    @property
    def pin(self):
        return self._pin
    @property
    def account_number(self):
        return self._acc_no
    

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        self.cards = {}
        self._lock = threading.Lock()
    def credit(self, amount):
        with self._lock:
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance-=amount
    def debit(self, amount):
        with self._lock:
            self.balance+=amount
    def get_balance(self):
        with self._lock:
            return self.balance
        

