import time
import threading
import logging
from infrastructure.habit_repository import HabitRepository

class HabitScheduler:
    def __init__(self):
        self.repo = HabitRepository()
        self.stop_thread = False  # Flag to stop the scheduler

        # Set up logging
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def check_habits(self):
        """Проверяет все привычки каждую секунду."""
        while True:
            now = int(time.time())
            habits = self.repo.get_all_habits()

            for habit in habits:
                start_date = habit["start_date"]
                period = habit["period"]
                next_due = habit.get("next_due", None)  # Используем сохраненное следующее выполнение
                last_completed = habit.get("last_completed", None)

                if next_due is None:  # Если `next_due` не существует, вычисляем его для первой итерации
                    cycles_passed = (now - start_date) // period
                    next_due = start_date + (cycles_passed + 1) * period
                    habit["next_due"] = next_due
                    self.repo.update_habit(habit["habit_id"], habit)

                #print(f"Current time (now): {now}, Next due time: {next_due}, Habit completed: {habit['is_completed']}")

                # Если время для выполнения пришло
                if now >= next_due and not habit["is_completed"]:
                    print(f"🔔 Время выполнить привычку: {habit['title']}!")
                    habit["is_completed"] = True  # Помечаем, что привычка выполнена
                    habit["last_completed"] = now  # Записываем время последнего выполнения
                    # Пересчитываем `next_due`
                    next_due = now + period  # Следующее выполнение через период
                    habit["next_due"] = next_due
                    self.repo.update_habit(habit["habit_id"], habit)

                # Если привычка выполнена, но уже прошло время для нового цикла — сбрасываем статус
                if habit["is_completed"] and last_completed and now >= next_due:
                    habit["is_completed"] = False
                    habit["last_completed"] = None  # Сбрасываем дату последнего выполнения
                    # Пересчитываем `next_due`
                    next_due = now + period  # Следующее выполнение через период
                    habit["next_due"] = next_due
                    self.repo.update_habit(habit["habit_id"], habit)
                    print(f"🔄 Привычка '{habit['title']}' сброшена на новый цикл.")

            time.sleep(1)  # Проверка каждую секунду


    def start(self):
        """Запускает планировщик в отдельном потоке."""
        thread = threading.Thread(target=self.check_habits, daemon=True)
        thread.start()

    def stop(self):
        """Останавливает планировщик."""
        self.stop_thread = True
