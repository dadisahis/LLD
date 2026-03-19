from Splitwise import Splitwise
from entities.Expense import Expense
from service.split_strategy import *
class DemoClass:
    @staticmethod
    def main():
        service  = Splitwise.get_instance()
        adi = service.add_user("Adi", "adi@mail.com")
        anu = service.add_user("Anu", "anu@mail.com")
        mee = service.add_user("Mee", "mee@mail.com")
        sai = service.add_user("Sai", "sai@mail.com")

        friend_group = service.add_group("Trip", [adi,anu, mee, sai])

        print("------------SETUP COMPLETE----------------")

        #Equal Split Expense
        service.create_expense(Expense.ExpenseBuilder().set_desc("Dinner").set_amount(1200).set_paid_by(adi).set_participants([adi, anu, mee, sai]).set_split_strategy(EqualSplitStrategry()))
        service.show_balance_sheet(adi.get_id())
        service.show_balance_sheet(anu.get_id())

        print("---------------------------------")

        service.create_expense(Expense.ExpenseBuilder().set_desc("Movie").set_amount(800).set_paid_by(anu).set_participants([adi, anu]).set_split_strategy(ExactSplitStrategy()).set_split_values([300, 500]))
        service.show_balance_sheet(adi.get_id())
        service.show_balance_sheet(anu.get_id())

        print("---------------------------------")
        print("--- Use Case 3: Percentage Split ---")
        service.create_expense(Expense.ExpenseBuilder()
                              .set_desc("Groceries")
                              .set_amount(500)
                              .set_paid_by(sai)
                              .set_participants([adi, anu, mee])
                              .set_split_strategy(PercentSplitStrategy())
                              .set_split_values([40.0, 30.0, 30.0]))  # 40%, 30%, 30%
        
        service.show_balance_sheet(adi.get_id())
        service.show_balance_sheet(anu.get_id())
        service.show_balance_sheet(mee.get_id())
        service.show_balance_sheet(sai.get_id())

        print("--- Use Case 4: Simplify Group Debts for 'Friends Trip' ---")
        simplified_debts = service.simplify_group_debt(friend_group.get_id())
        if not simplified_debts:
            print("All ddebs settled")
        else:
            for debt in simplified_debts:
                print(debt)


        print("---------------------------------")
        service.settle_up(anu.get_id(), sai.get_id(), 150)
        
        service.show_balance_sheet(adi.get_id())
        service.show_balance_sheet(anu.get_id())
        service.show_balance_sheet(mee.get_id())
        service.show_balance_sheet(sai.get_id())

        simplified_debts = service.simplify_group_debt(friend_group.get_id())
        if not simplified_debts:
            print("All ddebs settled")
        else:
            for debt in simplified_debts:
                print(debt)

        service.settle_up(mee.get_id(), adi.get_id(), 400)
        service.settle_up(mee.get_id(), sai.get_id(), 50)

        service.show_balance_sheet(adi.get_id())
        service.show_balance_sheet(anu.get_id())
        service.show_balance_sheet(mee.get_id())
        service.show_balance_sheet(sai.get_id())



if __name__ == '__main__':
    DemoClass.main()
