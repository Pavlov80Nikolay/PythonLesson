# Рантье (версия без ошибки)
# Демонстрирует логическую ошибку

print("Пргорамма подсчитывает ваши ежемесячные расходы.")
car = input("Техническое обслуживание машины: ")
car = int(car)
rent = input("Съем роскошной квартиры на Манхэттене: ")
rent = int(rent)
jet = input("Аренда самолета: ")
jet = int(jet)

# А можно и сразу превети к int
gifts = int(input("Подарки: "))
food = int(input("Обеды и ужины в ресторанах: "))
staff = int(input("Жалованье прислуги: "))
guru = int(input("Плата личному психоаналитику: "))
games = int(input("Компьютерные игры: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма: ", total)
