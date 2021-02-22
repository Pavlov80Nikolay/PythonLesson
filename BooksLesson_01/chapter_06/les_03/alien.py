# Создание пустого словаря

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# изменение значений в словаре
alien_0['color'] = 'yellow'
print(alien_0)

# удаление пар "ключ-значение"

del alien_0['color']
print(alien_0)

# Словарь с однотипными объектами
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
