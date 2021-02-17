# Создаем список квадратов всех целых чисел от 1 до 10

squares = []
# перебираем от 1 до 10 при помощи range()
for value in range(1, 11):
    # возводим во вторую степень, результат сохраняем в square
    square = value ** 2
    # каждое новое значение square присоединяем к списку squares
    squares.append(square)
    # 2 строки можно сделать более компактно - squares.append(value ** 2)

print(squares)
