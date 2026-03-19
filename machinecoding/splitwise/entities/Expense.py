from typing import Optional, List
from .User import User
from .Split import Split
from datetime import datetime
from service.split_strategy import SplitStrategy
class Expense:
    def __init__(self, expense: 'ExpenseBuilder'):
        self._id = expense._id
        self._desc = expense._desc
        self._amount = expense._amount
        self._paid_by = expense._paid_by
        self._timestamp = datetime.now()

        self._splits = expense._split_strategy.compute_split(expense._amount, expense._paid_by, expense._participants, expense._split_values)

    
    def get_id(self):
        return self._id
    
    def get_description(self) -> str:
        return self._desc
    
    def get_amount(self) -> float:
        return self._amount
    
    def get_paid_by(self) -> User:
        return self._paid_by
    
    def get_splits(self) -> List[Split]:
        return self._splits


    class ExpenseBuilder:
        def __init__(self):
            self._id: Optional[str] = None
            self._desc: Optional[str] = None
            self._amount: Optional[float] = None
            self._paid_by: Optional[User] = None
            self._participants: Optional[List[User]] = None
            self._split_strategy: Optional[SplitStrategy] = None
            self._split_values: Optional[List[float]] = None
    
        def set_id(self, id):
            self._id = id
            return self
        def set_desc(self, desc):
            self._desc = desc
            return self
        def set_amount(self, amount):
            self._amount= amount
            return self
        def set_paid_by(self, paid_by):
            self._paid_by = paid_by
            return self
        def set_participants(self, participants):
            self._participants = participants
            return self
        def set_split_strategy(self, split_strategy):
            self._split_strategy = split_strategy
            return self
        def set_split_values(self, split_values):
            self._split_values = split_values
            return self
        def build(self):
            if self._split_strategy is None:
                raise ValueError("Split Strategry cannot be none")
            return Expense(self)