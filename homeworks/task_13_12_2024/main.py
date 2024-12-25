import json
import os
import time
import random
import string

users=[]
def write(data):
    with open(base.txt,"w",encoding="utf-8") as file:
            file.write(data+"/n")
def read():
    with open(base.txt,"r",encoding="utf-8") as f:
               base.txt.append(line.strip())
def generate_id(length=16):
    timestamp = str(int(time.time() * 1000000))
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length-len(timestamp)))
        id_str = timestamp + random_chars
while True:
    print("Введите цифру 1 чтобы зарегистрироваться")
    print("Введите цифру 2 чтобы авторизоваться")
    a=input()
    if a=="1":
        email=input("Введите email")
        password=input("Введите пароль")
        user={"email" : email, "password" : password}
        users.append(user)
        users=map(str, users)
        str_users=",".join(users)
        str_users=write()

    elif a=="2":
        email=input()
        password=input()
       if os.path.isfile(base.txt):
           read()
           def check_authorization(email)
               if email and password in base.txt:
                   return True
               else:
                   print("Зарегистрирутесь пожалуйста")


    else:
         print("Ошибка ввода данных")
if check_authorization(True):
    b=input('''Для создание привычки напишите 1,
             Для получения списка всех привычек напишите 2 ''')
    if b==1:
        habit=input("Введите название привычки")
        habit=generate_id()





