import json
import os
import time
import random
import string
import auth
import habit
import system
import generator_id
import constants

users=[]
while True:
    #Обязательно даем информативные названия переменным !
    #Обзятально выносим в константы, чтобы не хардкодить !
    user_input = auth.handle_user_input()
    if user_input==constants.REGISTRATION:
        auth.handle_registration(users)
    elif user_input==constants.AUTH:
        auth.handle_login()
    else:
        auth.handle_error()


if auth.check_authorization(True):
    b=input('''Для создание привычки напишите 1,
             Для получения списка всех привычек напишите 2 ''')
    if b==1:
        habit=input("Введите название привычки")
        habit=generator_id.generate_id()





