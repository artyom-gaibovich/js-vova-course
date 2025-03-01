import database
habits_database = database.init_db('habits.json')




def find(title, description):
    input_habits = ''
    for habit in habits_database:
        if habit['title'] == title and habit['description'] == description:
            input_habit = habit
    if input_habit == '':
        print('Ошибка, пользователь не найден')
        return ''
    return input_habit



def create(title, description, ):
    habits_database.append({'title': title, 'description' : description})
    database.save(habits_database, 'habits.json')
