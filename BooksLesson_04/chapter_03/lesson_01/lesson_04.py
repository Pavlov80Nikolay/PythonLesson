# Компьютерный датчик настроения
# Демонстрирует использование elif

import random
print('Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.')
print('Итак, ваше настроение...')
mood = random.randint(1, 3)
if mood == 1:
    print('Радость')
elif mood == 2:
    print('Так себе')
elif mood == 3:
    print('Прескверное')
else:
    print('Не бывает такого настроения!')
print('Но это только сегодня')