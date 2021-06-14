# Эксклюзивная сеть
# Демонстрирует составление условия и логические операторы
print('\tЭксклюзивная компьютерная сеть')
print('\tТолько для зарегистрированных пользователей!\n')
security = 0
username = ""
while not username:
    username = input('Логин: ')
password = ""
while not password:
    password = input('Пароль: ')
if username == 'DM' and password == 'secret':
    print('Привет, Майк')
    security = 5
elif username == 'SM' and password == 'civil':
    print('Привет, Сид')
    security = 3
elif username == 'SMi' and password == 'mario':
    print('Привет, Сигеру')
    security = 3
elif username == 'WW' and password == 'thesims':
    print('Привет, Уилл')
    security = 3
elif username == 'user' and password == 'user':
    print('Привет, гость')
    security = 1
else:
    print('Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гость')

