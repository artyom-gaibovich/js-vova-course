import time
from infrastructure.habit_repository import HabitRepository


class NotifyHabit:
    def __init__(self):
        self.repo = HabitRepository()

    def execute(self):
        habits = self.repo.get_all_habits()
        now = int(time.time())

        for habit in habits:
            start_date = habit["start_date"]
            period = habit["period"]
            days_since_start = (now - start_date) // period
            next_due = start_date + (days_since_start + 1) * period

            if now >= next_due:
                print(f"Напоминание! Нужно выполнить привычку: {habit['title']}")
