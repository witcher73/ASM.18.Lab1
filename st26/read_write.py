# -*- coding: utf-8 -*-

from main_class import MainClass


class ReadWrite(MainClass):
    """
    Класс-потомок
    """
    number = ''

    def read_from_console(self):
        """
        Функция чтения с консоли
        """
        self.number = input('Введите номер: ')

    def print_to_console(self):
        """
        Функция вывода в консоль
        """
        print('Номер: ' + self.number)


if __name__ == '__main__':
    rw = ReadWrite()
    rw.read_from_console
    rw.print_to_console
