from abc import abstractmethod, ABC
from typing import List
from entities.User import User
from entities.Split import Split

class SplitStrategy(ABC):
    @abstractmethod
    def compute_split(self, total_amount: float, paid_by: User, participants:List[User], splits_vals: List[Split]):
        pass


class EqualSplitStrategry(SplitStrategy):
    def compute_split(self, total_amount, paid_by, participants, splits_vals):
        splits = []
        amount_per_person = total_amount / len(participants)
        for participant in participants:
            splits.append(Split(participant, amount_per_person))

        return splits
    

class ExactSplitStrategy(SplitStrategy):
    def compute_split(self, total_amount, paid_by, participants, splits_vals):
        if len(participants) != len(splits_vals):
            raise ValueError("Number of participants and values sould be equal")
        if abs(sum(splits_vals) - total_amount) > 0.01:
            raise ValueError("Sum of exact amounts must equal total amount")
        splits = []
        for i in range(len(participants)):
            splits.append(Split(participants[i], splits_vals[i]))

        return splits 
    
class PercentSplitStrategy(SplitStrategy):
    def compute_split(self, total_amount, paid_by, participants, splits_vals):
        if len(participants) != len(splits_vals):
            raise ValueError("Number of participants and values sould be equal")
        if abs(sum(splits_vals) - 100) > 0.01:
            raise ValueError("Sum of exact amounts must equal total amount")
        splits= []
        for i in range(len(participants)):
            amount = (total_amount * splits_vals[i])/100
            splits.append(Split(participants[i], amount))
        return splits