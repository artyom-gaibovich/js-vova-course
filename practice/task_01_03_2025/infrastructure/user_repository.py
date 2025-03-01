from infrastructure.database import Database
from domain.habit import Habit


class HabitRepository:
    def __init__(self):
        self.db = Database("habits.json")

    def add_habit(self, habit: Habit):
        habits = self.db.load_data()
        habits.append(habit.__dict__)
        self.db.save_data(habits)

    def get_all_habits(self):
        return self.db.load_data()

    def delete_habit(self, habit_id):
        habits = self.db.load_data()
        habits = [habit for habit in habits if habit["habit_id"] != habit_id]
        self.db.save_data(habits)

    def find_habit(self, habit_id):
        habits = self.db.load_data()
        for habit in habits:
            if habit["habit_id"] == habit_id:
                return habit
        return None

    def update_habit(self, habit_id, new_data):
        """Обновляет данные привычки."""
        habits = self.db.load_data()
        for habit in habits:
            if habit["habit_id"] == habit_id:
                habit.update(new_data)
        self.db.save_data(habits)
