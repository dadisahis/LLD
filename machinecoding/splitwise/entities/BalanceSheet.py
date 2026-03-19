from __future__ import annotations
import threading
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .User import User

class BalanceSheet:
    def __init__(self, owner: 'User'):
        self._owner = owner
        self._balances: Dict['User', float] = {}
        self._lock = threading.Lock()
    def get_balances(self):
        return self._balances
    
    def adjust_balance(self, user, amount):
        with self._lock:
            if self._owner == user:
                return
            new_amount = self._balances.get(user, 0.0) + amount
            if abs(new_amount) < 0.01:
                self._balances.pop(user, None)
            else:
                self._balances[user] = new_amount

    def get_net_balance(self):
        """Net balance across all other users.

        Positive means others owe this owner; negative means this owner owes others.
        """
        return sum(self._balances.values())

    def show_balances(self):
        print(f"Balance sheet for : {self._owner.get_name()}")
        if not self._balances:
            print("All Settled")
            return
        tot_owe_to_me = 0
        tot_owe_by_me = 0

        for user, amount in self._balances.items():
            if amount < -0.01:
                tot_owe_by_me+=(-amount)
            elif amount > 0.01:
                tot_owe_to_me+=amount


        print(f"Total Owed to {self._owner.get_name()}: {tot_owe_to_me}")
        print(f"Total Owed by {self._owner.get_name()}: {tot_owe_by_me}")
        print("-------------------------------------------")