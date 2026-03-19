import sys
sys.path.insert(0, 'machinecoding/splitwise')

from Splitwise import Splitwise
from entities.Expense import Expense
from service.split_strategy import EqualSplitStrategry, ExactSplitStrategy, PercentSplitStrategy

service = Splitwise.get_instance()
adi = service.add_user('Adi', 'adi@mail.com')
anu = service.add_user('Anu', 'anu@mail.com')
mee = service.add_user('Mee', 'mee@mail.com')
sai = service.add_user('Sai', 'sai@mail.com')

service.create_expense(
    Expense.ExpenseBuilder()
    .set_desc('Dinner')
    .set_amount(1200)
    .set_paid_by(adi)
    .set_participants([adi, anu, mee, sai])
    .set_split_strategy(EqualSplitStrategry())
)
service.create_expense(
    Expense.ExpenseBuilder()
    .set_desc('Movie')
    .set_amount(800)
    .set_paid_by(anu)
    .set_participants([adi, anu])
    .set_split_strategy(ExactSplitStrategy())
    .set_split_values([300, 500])
)
service.create_expense(
    Expense.ExpenseBuilder()
    .set_desc('Groceries')
    .set_amount(500)
    .set_paid_by(sai)
    .set_participants([adi, anu, mee])
    .set_split_strategy(PercentSplitStrategy())
    .set_split_values([40.0, 30.0, 30.0])
)

for u in [adi, anu, mee, sai]:
    print(f"{u.get_name()} balances:")
    for other, amt in u.get_balance_sheet().get_balances().items():
        print('  ', other.get_name(), amt)
    print('----')
