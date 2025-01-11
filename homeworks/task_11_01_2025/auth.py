import constants
import system


CONST_INPUT_LOGIN = "1"
CONST_INPUT_REGISTRATION = "2"
#TODO ПОДУМОЙ НАД НАЗВАНИЕМ ФАЙЛА (ЭТО же некий сервис, он что выполняет, значит и файл должен так называтся). Допустим auth_handler, или сам придумай пример названия.

def handle_registration(users):
    email=input(constants.CONST_HANDLE_REGISTRATION_EMAIL)
    password=input(constants.CONST_HANDLE_REGISTRATION_PASS)
    user={"email" : email, "password" : password}
    users.append(user)
    users=map(str, users)
    str_users=",".join(
    )
    str_users=system.write()
def handle_login():
    email=input()
    password=input()
    # РАБОТУ С ФАЙЛОВЫМИ ПУТЯМИ НАДО ВЫНОСИТЬ В ОТДЕЛЬНЫЙ СЕРВИС !!!


    #TODO Поправить
    # 1 Функция - 1 Зона ответственности, те функция не должна выполнять много действий (к примеру авторизация не должна заниматься чтением файлов, она
    # она должна заниматься авторизацией !)
    if os.path.isfile(base.txt):
        read()
        check_authorization(email)


def handle_user_input():
  user_input = input(constants.CONST_HANDLE_USER_INPUT)
  if (user_input == CONST_INPUT_LOGIN):
    print(constants.AUTH)
    return constants.AUTH
  elif (user_input == CONST_INPUT_REGISTRATION):
    print(constants.REGISTRATION)
    return constants.REGISTRATION
  else:
    print(constants.ERROR)
    return constants.ERROR

def check_authorization(email):

    if email and password in base.txt:
        return True
    else:
        print(constants.CONST_CHECK_INPUT)