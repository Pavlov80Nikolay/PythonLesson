# чтобы вставить значение переменной в строку, поставьте букву f непосредственно перед кавычками

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(full_name)

# а можно и так

print(f'Hello, {full_name.title()}!')

# F-строками можно воспользоваться для построения сообщения, которое затем сохранить в переменной
# message = f'Hello, {full_name.title()}!'
