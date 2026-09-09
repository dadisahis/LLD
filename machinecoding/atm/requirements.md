Functional Requirements:
 - Authenticate users via card number and PIN
 - Support 3 transactions: Withraw, Deposit and Balance inquiry
 - Dispense cash - largest denom first($100, $50, $20, $10)
 - Validate both account balance and ATM cash inventory before dispensing.
 - Track ATM State transactions - idle, card inserted, authenticated
 - Simulate Bank Opertations(auth, balance check, debit, credit) via an in memory service


 NFR: 
 - Should follow OOps and should be modular
 - Thread safe
 - components should be testable in isolation

Entities
 - Transcation Type:Enum  Withdraw, Balance and Deposit  
 - ATM State: IDLE, CARD_INSERTED, AUTHENTICATED
 - Denominations: 100, 50, 20, 10
 - Card: Data Class:  Card Number and PIN
 - Account - Account No, Balance
 - Transaction - Data class: type, amount, timestamp
 - Cash Dispenser - 
 - Bank Service - manages, cards, accounts, auth and balance operations
 - ATM - Orchestrator- accepts, cards, delegate auth, coordinate transcation, manage state transitions. Singleton as there can be just one physical system and needs to be consistent accross all operations
 