import datetime
import generator_id
import id
import time
habits=[]
def handle_error():
     print("Ошибка ввода данных")
def create_habit():
    #TODO сделать логику создания привычки
    new_habit= {
               name:input("Введите имя привычки"),
               description=input("Введите описание привычки")
               new_habit_id:generator_id.generate_id(),
               start_date=datetime.today(),
               is_resolve:False

    }
def delete_habit():
    #TODO сделать логику удаления привычки
    object_id=id(habits[input("Напишите ваше id")])
    for i,obj in enumerate habits:
        if id(obj)==object_id:
            del habits[i]
def edit_habit():
    #TODO сделать логику редактирования привычки
    a=int(input("Введите id вашей привычки"))
        for i in habits.txt:
            if i==a:
                    new_habit={
                                name=input()
                                description=input()
                              }
def check_habits():
    #TODO сделать логику представления всех привычки
    for i in range(0, len(habits.txt)):
        print(habits.txt[i])
def check_habit():
    #TODO сделать логику представления одной привычки
    current_day=datetime.today()
    interval=86400
    days_start_to_current = (current_date - start_date) // interval
    next_day = start_date + (days_start_to_current + 1) * interval
    formatted_next_day = timestamp_converter(next_day)
    a=int(input("Введите id вашей привычки"))
    for i in habits.txt:
        if i==a:
            i=current_habit_id
    fullfiled(current_habit_id)
    if is_fullfilled=False:
        1=1
    elif is_fullfilled= True:
        print(f"Привычка была исполнена на период с {formatted_day_before} по {formatted_next_day}")
    elif is_fullfilled= "Fail":
        print(f"Привычка не была исполнена на период с {formatted_day_before} по {formatted_next_day}")


