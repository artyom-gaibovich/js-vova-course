import datetime
import generator_id
habits=[]
def handle_error():
     print("Ошибка ввода данных")
def create_habit():
    #TODO сделать логику создания привычки
    period=input("Напишите,ваша привычка будет повторятся каждый день,каждую неделю или каждый месяц?")
    if period=="каждый день":
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=1)
    elif period=="каждый месяц":
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=30)
    elif period=="каждую неделю":
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=7)
    else:
        print("Ошибка ввода данных")
    time_str=input("Введите время в формате час-минута-секунда")
    new_habit= {
               name:input("Введите имя привычки"),
               new_habit_id:generator_id.generate_id(),
               period:5,
               time:datetime.strtime(time_str, '%H-%M-%S'),
    }
def delete_habit():
    #TODO сделать логику удаления привычки
    index=habits.index(new_habit_id)
    habits.remove(index)
def edit_habit():
    #TODO сделать логику редактирования привычки
    pass
def get_habits():
    #TODO сделать логику представления всех привычки
    for i in range(0, len(habits)):
        print(habits[i])
def get_habit():
    #TODO сделать логику представления одной привычки
    index=habits.index(new_habit_id)
    print(index)