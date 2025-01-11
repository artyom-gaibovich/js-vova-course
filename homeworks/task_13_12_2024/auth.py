
def handle_registration():
    email=input("Введите email")
    password=input("Введите пароль")
    user={"email" : email, "password" : password}
    users.append(user)
    users=map(str, users)
    str_users=",".join(users)
    str_users=write()
def handle_login():
    email=input()
    password=input()
    if os.path.isfile(base.txt):
        read()
        check_authorization(email)
def handle_user_input():
  user_input = input("Введите 1 для авторизации, введите 2 для регистрации\n")
  if (user_input == "1"):
    print("Авторизация")
  elif (user_input == "2"):
    print("Регистрация")
  else:
    print("Ошибка")
def check_authorization(email):

    if email and password in base.txt:
        return True
    else:
        print("Зарегистрирутесь пожалуйста")