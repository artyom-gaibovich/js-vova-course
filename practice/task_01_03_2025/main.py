from use_cases.create_habit import CreateHabit
from use_cases.delete_habit import DeleteHabit
from use_cases.check_habits import CheckHabits
from use_cases.manage_habit import
from use_cases.schedule_habits import HabitScheduler

def main():
    scheduler = HabitScheduler()
    scheduler.start()  # Запускаем проверку привычек

    while True:
        choice = input("\n1 - Создать привычку\n2 - Удалить привычку\n3 - Посмотреть привычки\n4 - Отметить выполненной\n5 - Выход\nВаш выбор: ")

        if choice == "1":
            title = input("Название: ")
            description = input("Описание: ")
            period = int(input("Период (в секундах): "))
            CreateHabit().execute(title, description, period)

        elif choice == "2":
            habit_id = input("ID привычки: ")
            DeleteHabit().execute(habit_id)

        elif choice == "3":
            CheckHabits().execute()

        elif choice == "4":
            habit_id = input("ID привычки: ")
            ManageHabit().mark_completed(habit_id)

        elif choice == "5":
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
