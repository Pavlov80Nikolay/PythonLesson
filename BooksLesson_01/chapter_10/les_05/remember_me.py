"""Сохранение и чтение данных, сгенерированных пользователем"""

import json

username = input('Как тебя зовут? ')

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f'Привет, {username}!')
