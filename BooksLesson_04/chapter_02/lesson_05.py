# Манипуляции с цитатой
# Демонстрирует строковые методы
# цитата из Томаса Уотсона, который в 1943 г. был директором IBM

quote = "Думаю, на мировом рынке можно будет продать штук 5 компьютеров"

print("Исходная цитата: ")
print(quote)
print("\nОна же в верхнем регистре:")
print(quote.upper())
print("\nВ нижнем регистре")
print(quote.lower())
print("\nКак заголовок")
print(quote.title())
print("\nС ма-а-ленькой заменой")
print(quote.replace("штук 5", "несколько миллионов"))