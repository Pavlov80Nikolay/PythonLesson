# Создание класса Dog

class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f'{self.name} rolled over!')
