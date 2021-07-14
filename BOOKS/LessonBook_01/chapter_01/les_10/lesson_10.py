# функция для отображения букв из переданного аргументом текста
def show(txt):
    # преобразование текста в список и его сортировка
    symbs = sorted(list(txt))
    # отображение содержимого списка
    print(symbs)
# вызов функции
show('Python')
# функция для вычисления суммы квадратов натуральных чисел
def sqsum(n):
    # создание списка из квадратов натуральных чисел
    nums = [k*k for k in range(1, n+1)]
    # результат функции
    return sum(nums)
# переменная с числовым значением
m = 10
# вызов функции для вычисления суммы квадратов чисел
print('Сумма квадратов чисел от 1 до', str(m) + ':', sqsum(m))
