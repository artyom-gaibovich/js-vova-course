from infrastructure.habit_repository import HabitRepository


class DeleteHabit:
    def __init__(self):
        self.repo = HabitRepository()

    def execute(self, habit_id):
        self.repo.delete_habit(habit_id)
        print(f"Привычка {habit_id} удалена!")
