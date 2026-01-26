from abc import ABC, abstractmethod

class FitnessDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass

class FitnessDataSubject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass
    @abstractmethod
    def notifyObserver(self):
        pass


class FitnessData(FitnessDataSubject):
    def __init__(self):
        self.steps = 0
        self.active_mins = 0
        self.calories = 0
        self.observers = []

    def registerObserver(self, observer):
       self.observers.append(observer)
    
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObserver(self):
        for obs in self.observers:
            obs.update(self)

    def new_data_published(self, strps, act_mins, cal):
        self.steps = strps
        self.active_mins = act_mins
        self.calories = cal

        print("New fitness data published:")
        print(f"Steps: {self.steps}, Active Minutes: {self.active_mins}, Calories: {self.calories}\n")

        self.notifyObserver()
    
    def daily_reset(self):
        self.steps=0
        self.active_mins=0
        self.calories=0
        print("Daily fitness data reset.\n")
        self.notifyObserver()
    def get_steps(self):
        return self.steps
    def get_active_mins(self):
        return self.active_mins
    def get_calories(self):
        return self.calories

class LiveActivityDisplay(FitnessDataObserver):
    def update(self, data):
        print("Live Activity Display Updated:")
        print(f"Steps: {data.steps}, Active Minutes: {data.active_mins}, Calories: {data.calories}\n")


class ProgressLogger(FitnessDataObserver):
    def update(self, data):
        print("Progress Logger Updated:")
        print(f"Steps: {data.steps}, Active Minutes: {data.active_mins}, Calories: {data.calories}\n")

class GoalNotifier(FitnessDataObserver):
    def __init__(self):
        self.daily_goal = 10000
        self.goal_reached = False
    
    def update(self, data):
        if data.get_steps() >= self.daily_goal and not self.goal_reached:
            print("Goal Notifier: Congratulations! You've reached your daily step goal!\n")
            self.goal_reached = True

    def reset(self):
        self.goal_reached = False


