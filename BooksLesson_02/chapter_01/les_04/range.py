#TODO Эксперементы с диапазонами, RANGE - в разных примерах


x = range(5)
print(x)

# передадим вывод "range" функции "list", чтобы получить список
y = list(range(5))
print(y)

# мы можем задать НАЧАЛЬНОЕ и КОНЕЧНОЕ значение для "range"
q = list(range(5, 10))
print(q)

# мы также можем задать значение ШАГА
w = list(range(0, 10, 2))
print(w)

# можно задать ОТРИЦАТЕЛЬНОЕ значение
e = list(range(10, 0, -2))
print(e)

t = list(range(99, 0, -1))
print(t)
