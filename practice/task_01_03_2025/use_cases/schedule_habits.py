import time
import threading
from infrastructure.habit_repository import HabitRepository


class HabitScheduler:
    def __init__(self):
        self.repo = HabitRepository()

    def check_habits(self):
        """Проверяет все привычки каждую секунду."""
        while True:
            now = int(time.time())
            habits = self.repo.get_all_habits()

            for habit in habits:
                start_date = habit["start_date"]
                period = habit["period"]
                last_completed = habit.get("last_completed", None)

                # Определяем следующее время выполнения
                days_since_start = (now - start_date) // period
                next_due = start_date + (days_since_start + 1) * period

                # Если привычка еще не выполнена и пришло время — напоминаем
                if now >= next_due:
                    if not habit["is_completed"]:
                        print(f"🔔 Время выполнить привычку: {habit['title']}!")

                # Если привычка выполнена, но уже прошло время для нового цикла — сбрасываем статус
                if habit["is_completed"] and last_completed and now >= next_due:
                    habit["is_completed"] = False
                    self.repo.update_habit(habit["habit_id"], habit)
                    print(f"🔄 Привычка '{habit['title']}' сброшена на новый цикл.")

            time.sleep(1)  # Проверка каждую секунду

    def start(self):
        """Запускает планировщик в отдельном потоке."""
        thread = threading.Thread(target=self.check_habits, daemon=True)
        thread.start()
