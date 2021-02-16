# Упорядочение списка
# постоянная сортировка списка методом sort(), по алфавиту (на постоянной основе, то есть вернуть к исходному порядку НЕЛЬЗЯ)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# в обратном порядке
cars.sort(reverse=True)
print(cars)

# Временная сортировка списка функцией sorted()
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars2)

print('\nHere is the original list:')
print(sorted(cars2))

print('\nHere is the original list:')
print(cars2)

# Вывод списка в обратном порядке (используетмя метод reverse()) - он тоже осуществляет постоянное изменение
cars2.reverse()
print(cars2)

# Определение длины списка
print(len(cars2))