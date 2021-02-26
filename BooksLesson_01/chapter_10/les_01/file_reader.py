"""Программа открывает, читатет его и выводит содержимое на экран"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
