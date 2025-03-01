from domain.habit import Habit
from infrastructure.database import Database  # Импортируем класс Database
class HabitRepository:
    def __init__(self):
        self.db = Database("habits.json")

    def add_habit(self, habit: Habit):
        habits = self.db.load_data()
        #print(f"Adding habit: {habit.__dict__}")  # Логируем добавление
        habits.append(habit.__dict__)  # Добавляем привычку в список
        self.db.save_data(habits)

    def get_all_habits(self):
        habits = self.db.load_data()
        #print(f"Loaded habits: {habits}")  # Логируем загрузку данных
        return habits

    def delete_habit(self, habit_id):
        habits = self.db.load_data()
        print(f"Deleting habit with id {habit_id}")  # Логируем удаление
        #habits = [habit for habit in habits if habit["habit_id"] != habit_id]
        self.db.save_data(habits)

    # В файле habit_repository.py
    def update_habit(self, habit_id, updated_habit):
        habits = self.db.load_data()
        for index, habit in enumerate(habits):
            if habit["habit_id"] == habit_id:
                #print(f"Updating habit {habit_id} to {updated_habit}")  # Логируем обновление
                habits[index] = updated_habit  # Обновляем привычку, если это словарь
                self.db.save_data(habits)
                return True
        return False

