import random
class Dice:
    def __init__(self, minVal: int, maxVal: int):
        self.minVal = minVal
        self.maxVal = maxVal

    def roll_dice(self):
        return random.randint(self.minVal, self.maxVal)