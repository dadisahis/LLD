import threading
from typing import Dict
from entities.User import User
from entities.Group import Group
from entities.Expense import Expense
from entities.Transaction import Transaction
import heapq
class Splitwise:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized=False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._users: Dict[str, User] = {}
            self._groups: Dict[str, Group] = {}
            self._initialized = True


    @classmethod
    def get_instance(cls):
        return cls()
    
    def add_user(self, name, email):
        user = User(name, email)
        self._users[user.get_id()] = user
        return user
    
    def add_group(self, name, members):
        group = Group(name, members)
        self._groups[group.get_id()] = group
        return group
    

    def get_user(self, user_id):
        return self._users.get(user_id, None)
    def get_group(self, group_id):
        return self._groups.get(group_id, None)
    
    def create_expense(self, builder: Expense.ExpenseBuilder):
        with self._lock:
            expense = builder.build()
            paid_by  = expense.get_paid_by()

            for split in expense.get_splits():
                participant = split.get_user()
                amount = split.get_amount()
                if paid_by!= participant:
                    paid_by.get_balance_sheet().adjust_balance(participant, amount)
                    participant.get_balance_sheet().adjust_balance(paid_by, -amount)
            print(f"Expense {expense.get_description()} of amount {expense.get_amount()} created")
    
    def settle_up(self, payer_id, payee_id, amount):
        with self._lock:
            payer = self._users[payer_id]
            payee = self._users[payee_id]
            print(f"{payer.get_name()} is settling up {amount} with {payee.get_name()}")
            payee.get_balance_sheet().adjust_balance(payer, -amount)
            payer.get_balance_sheet().adjust_balance(payee, amount)

    def show_balance_sheet(self, user_id):
        user = self._users[user_id]
        user.get_balance_sheet().show_balances()

    def simplify_group_debt(self, group_id):
        group  = self._groups.get(group_id, None)
        if not group:
            raise ValueError("Group not found")
        net_balances = {}
        for mem in group.get_members():
            balance = 0
            for other_user, amount in mem.get_balance_sheet().get_balances().items():
                if other_user in group.get_members():
                    balance += amount
            net_balances[mem] = balance

        # Separate into creditors and debtors
        creditors = [(user, balance) for user, balance in net_balances.items() if balance > 0]
        debtors = [(user, balance) for user, balance in net_balances.items() if balance < 0]
        
        creditors.sort(key=lambda x: x[1], reverse=True)
        debtors.sort(key=lambda x: x[1])

        transactions = []
        i=j=0
        while i < len(creditors) and j < len(debtors):
            cred_user, cred_amount = creditors[i]
            deb_user, deb_amount = debtors[j]

            amt_to_settle = min(cred_amount, -deb_amount)
            transactions.append(Transaction(deb_user, cred_user, amt_to_settle))

            creditors[i] = (cred_user, cred_amount - amt_to_settle)
            debtors[j] = (deb_user,  deb_amount + amt_to_settle)

            if abs(creditors[i][1]) < .01:
                i+=1
            if abs(debtors[j][1]) < 0.01:
                j+=1
        return transactions


    