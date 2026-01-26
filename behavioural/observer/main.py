from observer import *


def main():
    fitness_data = FitnessData()

    activity_obserever = LiveActivityDisplay()
    progress_observer = ProgressLogger()
    goal_observer = GoalNotifier()

    fitness_data.registerObserver(activity_obserever)
    fitness_data.registerObserver(progress_observer)
    fitness_data.registerObserver(goal_observer)

    fitness_data.new_data_published(5000, 30, 200)
    fitness_data.new_data_published(7000, 60, 500)
    fitness_data.new_data_published(10000, 75, 800)

    goal_observer.reset()
    fitness_data.daily_reset()

if __name__ == "__main__":
    main()
