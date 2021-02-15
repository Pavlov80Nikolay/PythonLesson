# Изменение, добавление и удаление элементов
# Изменение элементов списка

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Добавление элеметов в список

motorcycles.append('honda')
print(motorcycles)

# метод append() упращает динамическое построение списков. Вы можете начать с пустого списка и добавить в него элеметы
motor = []
motor.append('honda')
motor.append('ducati')
motor.append('yamaha')
print(motor)

# Вставка элемента в список
motor.insert(0, 'suzuki')
print(motor)

# Удаление элементов из списка
del motor[0]
print(motor)

# Уделение элементов по значению
motor.remove('ducati')
print(motor)

# Извлечение элементов из произвольной позиции списка
