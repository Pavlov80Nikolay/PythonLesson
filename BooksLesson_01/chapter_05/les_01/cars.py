# Проверка равенство

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Проверка не равенства
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# так же можно и с числами
answer = 17

if answer != 42:
    print('That is not correct answer. Please try again!')

