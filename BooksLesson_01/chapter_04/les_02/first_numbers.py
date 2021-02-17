# Функция range()
# упрощает построение числовых последовательностей. С ее помощью легко вывести серию чисел
# в этом примере выводится только числа от 1 до 4, можно начинать и с 0(нуля)
for value in range(1, 5):
    print(value)

# Использование range() для создания числового списка
number = list(range(1, 6))
print(number)

# range() также может пропускать числа в заданном диапазоне
# в примере, начинается с 2 и затем увеличивает его на 2
even_number = list(range(2, 11, 2))
print(even_number)

