import datetime
import generator_id
habits=[]

#TODO ПОДУМОЙ НАД НАЗВАНИЕМ ФАЙЛА (ЭТО же некий сервис, он что выполняет, значит и файл должен так называтся). Допустим habit_service, или сам придумай пример названия.

def handle_error():
     print("Ошибка ввода данных")
def create_habit():
    #TODO Вынести сообщения в отдельые константы, чтобы не было ХАРДКОДИНГА !
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