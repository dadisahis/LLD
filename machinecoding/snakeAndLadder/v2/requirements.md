Functional Requirements:
1. Configurable number of players
2. Configurable ladder and Snakes and Board Size
3. Simulate Dice rolls
4. If player moves to a position occupied by someone else, dont do anything, both standd in the position
5. if user rolls dice which leads to out of bound, skip

Non Functional Requirements:
1. Project should follow OOPs
2. Easily testable
3. Easy to extend and maintain


Entities:
1. Status: Enum depicting Game Status, NOT STARTED, PLAYING, FINISHED
2. Player: Data class holding player meta data
3. Game Entity: Abstract class depicting en entity like snake or ladder
4. SnakeEntity and LadderEntity, concrete implentations of Game Entity
5. Boardd:Board meta data class
6. Game: Main Service orchestrating Game play
7.  Dice: to simulate dice roll
