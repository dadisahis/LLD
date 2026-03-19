LLD - Splitwise


Requirements:
1. Add Users
2. Create groups
3. Add expense with different split type: equal, exact and percent
4. Track pairwise net balances b/w users(who owes whom and how much)
5. Support partial and full settlements


Core Entities and classes
1. SplitType : Enum - split categories(Equal,Exact, Percentage)
2. User: Data class : User Profile(id, name, email, phone) 
3. Split: Data Class : Track a participant user id and owed amount
4. Expense: Data class: Records who paid, how much and how it was split
5. Group: Data class: Container for users and expense
6. SplitStrategy:  Interface: Contract for split validation and calculation
7. Balance Sheet: Core Class: Pair wise net debt tracking(adjacency matrix)
8. SplitwiseService: Core class: Orchestrates expenes, settlements, and notifications

