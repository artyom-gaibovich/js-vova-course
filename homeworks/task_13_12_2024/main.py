import json
users=[]
def write(data):
    with open(base.txt,"w",encoding="utf-8") as file:
            file.write(data+"/n")
def read():
    with open(base.txt,"r",encoding="utf-8") as file:
                 content=file.readlines()
                 return [line.strip()for line in content]
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
        if email=base.txt:

    else:
         print("Ошибка ввода данных")


