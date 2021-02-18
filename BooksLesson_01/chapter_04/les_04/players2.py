# Перебор содержимого сегмента
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# в этом примере программа перебирает первых 3 игроков и выводит их имена
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

