# -*- coding: utf-8 -*-


class MainClass:
    name = ''
    age = ''
    job = ''

    def read_from_console(self):
        """
        Функция чтения с консоли
        """
        self.name = input('Введите имя: ')
        self.age = input('Введите возраст: ')
        self.job = input('Введите должность: ')

    def print_to_console(self):
        """
        Функция вывода в консоль
        """
        print('\nИмя: ' + self.name)
        print('Возраст: ' + self.age)
        print('Должность: ' + self.job)


if __name__ == '__main__':
    mc = MainClass()
    mc.read_from_console
    mc.print_to_console
