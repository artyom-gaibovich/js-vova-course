import datetime
habits=[]
def generate_id(length=16):
    timestamp = str(int(time.time() * 1000000))
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits,k=length-len(timestamp)))
    id_str = timestamp + random_chars
def handle_error():
     print("Ошибка ввода данных")
def create_habit():
    #TODO сделать логику создания привычки
    period=input("Напишите,ваша привычка будет повторятся каждый день,каждую неделю или каждый месяц?")
    if period=="каждый день":
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=1)
    elif period=="каждый месяц"
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=30)
    elif period="каждую неделю":
        date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        date = datetime.strtime(date_str, '%Y-%m-%d')
        period=date+datetime.timedelta(days=7)
    else:
        print("Ошибка ввода данных")

    new_habit= {
               name=input("Введите имя привычки")
               new_habit_id=generate_id()
               print(period)
               time_str=input("Введите время в формате час-минута-секунда")
               time=datetime.strtime(time_str, '%H-%M-%S')

    }
def delete_habit():
    #TODO сделать логику удаления привычки

def edit_habit():
    #TODO сделать логику редактирования привычки
def get_habits():
    #TODO сделать логику представления всех привычки
def get_habit():
    #TODO сделать логику представления одной привычки