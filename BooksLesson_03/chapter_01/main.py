"""Лекция 1"""

# Округление чисел функцией round()

f = 5.1575
print(round(f))
print(round(f, 2))

# Порой, числа приходят не в том формате, в котором мы бы хотели их видеть
# при помощи функций: int() и float(), мы можем перевести к типу числа
s = '5'

print(int(f))
print(int(s))
# или так например
print(float(s))