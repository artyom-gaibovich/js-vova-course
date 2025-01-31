import user_repository

def login(username, password):
    user = user_repository.find(username, password)
    if user == '':
        print('Юзер не найден')
    return user


def register(username, password, age):
    user_repository.create(username, password,age)

