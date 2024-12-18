import json
import os
users=[]
def write(data):
    with open(base.txt,"w",encoding="utf-8") as file:
            file.write(data+"/n")
def read():
    with open(base.txt,"r",encoding="utf-8") as f:
               base.txt.append(line.strip())
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
       if os.path.isfile(base.txt):
           read()
           def check_authorization(email)
               if email in base.txt:
                   return True
               else:
                   print("Зарегистрирутесь пожалуйста")


    else:
         print("Ошибка ввода данных")



