from domain.habit import Habit
from infrastructure.habit_repository import HabitRepository


class CreateHabit:
    def __init__(self):
        self.repo = HabitRepository()

    def execute(self, title, description, period):
        habit = Habit(title, description, period)
        self.repo.add_habit(habit)
        print(f"Привычка '{title}' создана!")
