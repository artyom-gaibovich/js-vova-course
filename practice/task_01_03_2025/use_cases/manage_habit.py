from infrastructure.habit_repository import HabitRepository
import time


class ManageHabit:
    def __init__(self):
        self.repo = HabitRepository()

    def mark_completed(self, habit_id):
        """Отметить привычку как выполненную."""
        habit = self.repo.find_habit(habit_id)
        if habit:
            habit["is_completed"] = True
            habit["last_completed"] = int(time.time())
            self.repo.update_habit(habit_id, habit)
            print(f"Привычка '{habit['title']}' отмечена как выполненная.")
        else:
            print("Привычка не найдена.")
