


Functional Requirements:
1. Game played on a 10x10 boardd
2. support config of snakes and ladders on a board
3. Snake sends the player back to lower config square and Ladder moves the player up
4. Allow multiple players(min: 2), with round robin turn
5. Simulate dice rolls with a 6 causing an extra roll
6. Player must roll exact number to land on cell 100 and win game
7. Multiple players can occupy same cell without interaction


Core Entities:
1. Board -> Core Class
2. BoardEntity -> Abstract Class -> Snake and Ladder (start and end position) -> Data Class
3. User -> Data Class
4. Dice -> Core Class
5. Game -> Core Class -> Orchestrator ->  roll dice, move player,check for entity, check for win, and roll extra on a 6
6. GameStatus -> Enum-> NOT_STARTED, RUNNING, FINISHED
