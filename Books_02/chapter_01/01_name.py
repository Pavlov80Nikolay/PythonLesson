# TODO Строки, изменение строк

name = 'ada lovelace'

# метод title() - преобразует первые символы каждого слова в строке в верхнему
print(name.title())

# все символы - к верхнему и нижнему регистру
name2 = 'Ada Lovelace'
print(name2.upper())
print(name2.lower())

# использование переменных в строках
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

# можно например так
print(f'Hello, {full_name.title()}')

# а можно и так, а получится тоже самое
message = f'Hello, {full_name.title()}'
print(message)

















