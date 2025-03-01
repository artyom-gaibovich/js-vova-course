
import json


def init_db(path_to_db):
    with open(path_to_db, 'r') as json_file:
        users_database = json.load(json_file)
    return users_database


def save(new_users_database, path_to_db):
    with open(path_to_db, 'w') as json_file:
        json.dump(new_users_database, json_file)
