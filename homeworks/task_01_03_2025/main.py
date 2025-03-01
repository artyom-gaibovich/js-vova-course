import json
import os
import time
import random
import string
import auth
import habit
import system
import generator_id
users=[]

while True:
    auth.handle_user_input()
    if a=="1":
        auth.handle_registration()
    elif a=="2":
       auth.handle_login()
    else:
        auth.handle_error()
if auth.check_authorization(True):
    b=input('''Для создание привычки напишите 1,
             Для получения списка всех привычек напишите 2 ''')
    if b==1:
        habit=input("Введите название привычки")
        habit=generator_id.generate_id()





