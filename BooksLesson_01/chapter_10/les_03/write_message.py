"""Присоединение данных к файлу"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love ...\n')
    file_object.write('I love creating apps ...\n')

