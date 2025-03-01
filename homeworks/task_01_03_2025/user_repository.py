import database
users_database = database.init_db('users.json')


def find(username, password):
    input_user = ''
    for user in users_database:
        if user['username'] == username and user['password'] == password:
            input_user = user
    if input_user == '':
        print('Ошибка, пользователь не найден')
        return ''
    return input_user



def create(username, password, age):
    users_database.append({'username': username, 'password' : password, 'age' : age})
    database.save(users_database, 'users.json')
