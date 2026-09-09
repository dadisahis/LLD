from enum import Enum

class TransactionType(Enum):
    WITHDRAWAL = "WITHDRAWAL"
    DEPOSIT = "DEPOSIT"
    BALANCE_INQUIRY = "BALANCE_INQUIRY"


class ATMState(Enum):
    IDLE = "IDLE"
    CARD_INSERTED = "CARD_INSERTED"
    AUTHENTICATED = "AUTHENTICATED"


class Denom(Enum):
    HUNDRED=100
    FIFTY=50
    TWENTY=20
    TEN=10