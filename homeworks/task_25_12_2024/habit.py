import datetime
import generator_id
import id
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
               description=input("Введите описание привычки")
               new_habit_id:generator_id.generate_id(),
               period:5,
               time:datetime.strtime(time_str, '%H-%M-%S'),
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
    id(input("Введите id привычки,которую вы хотите отредактировать")
    if id==new_habit_id in habits:
         new_habit={
                 name=input()
                 description=input()
                 period=input()
                 time_str=input("Введите время в формате час-минута-секунда")
         }
def check_habits():
    #TODO сделать логику представления всех привычки
    for i in range(0, len(habits)):
        print(habits[i])
def check_habit():
    #TODO сделать логику представления одной привычки
    index=habits.index(new_habit_id)
    print(index))
    if datetime.now()<end_date:
        is_resolve=True
    else:
        is_resolve=False
        print("Вы не выполнили привычку")
