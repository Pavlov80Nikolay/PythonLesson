# Перебор всего списка

magicians = ['alice', 'david', 'carolina']
# цикл for. Строка приказывает взять очередное имя из списка и сохранить его в переменной magician
for magician in magicians:
    print(magician)

    print(f'{magician.title()}, that was a great trick!')

    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Этот код будет выполнен после цикла For
print('Thank you, everyone. That was a great magic show!')
