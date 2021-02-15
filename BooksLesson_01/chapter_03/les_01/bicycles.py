# Списки

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# индекс начинается с 0, а не с 1
print(bicycles[0])

print(bicycles[2])

# но можно и отформатировать
print(bicycles[0].title())


# использование отдельных элементов из списка
message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)
