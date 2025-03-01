from infrastructure.habit_repository import HabitRepository


class CheckHabits:
    def __init__(self):
        self.repo = HabitRepository()

    def execute(self):
        habits = self.repo.get_all_habits()
        if not habits:
            print("Нет привычек.")
        else:
            for habit in habits:
                print(f"{habit['title']} - {habit['description']}")
