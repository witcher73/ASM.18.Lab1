# -*- coding: utf-8 -*-

import pickle
from time import sleep
from os import system

from read_write import ReadWrite


class Container(ReadWrite):
    """
    Контейнерный класс
    """
    group = ''
    company = ''
    students = []
    teachers = []
    other = []

    def __init__(self, t):
        self.t = t

    def add_list(self):
        """
        Добавление новых записей в список
        """
        ReadWrite.name = input('Введите имя: ')
        ReadWrite.age = input('Введите возраст: ')
        ReadWrite.number = input('Введите телефон: ')
        if self.t == 'students':
            self.group = input('Введите номер группы: ')
            self.students.append('Имя:{0}, Возр:{1}, Тел:{2}, Группа:{3}'.format
                                 (
                                  ReadWrite.name,
                                  ReadWrite.age,
                                  ReadWrite.number,
                                  self.group
                                  )
                                 )
        elif self.t == 'teachers':
            ReadWrite.job = input('Введите должность: ')
            self.teachers.append('Имя:{0}, Возр:{1}, Тел:{2}, Должность:{3}'.format
                                 (
                                  ReadWrite.name,
                                  ReadWrite.age,
                                  ReadWrite.number,
                                  ReadWrite.job
                                  )
                                 )
        elif self.t == 'other':
            self.company = input('Введите название компании: ')
            ReadWrite.job = input('Введите должность: ')
            self.other.append('Имя:{0}, Возр:{1}, Тел:{2}, Компания:{3}, Должность:{4}'.format
                              (
                               ReadWrite.name,
                               ReadWrite.age,
                               ReadWrite.number,
                               self.company,
                               ReadWrite.job
                               )
                              )
        system('clear')
        print('\n{0} добавлен в список.'.format(ReadWrite.name))
        sleep(2)

    def get_list(self):
        """
        Вывод списка
        """
        if self.t == 'students':
            print(self.students)
        elif self.t == 'teachers':
            print(self.teachers)
        elif self.t == 'others':
            print(self.other)
        input('Для продолжения нажмите ENTER')  # задержка возврата в меню

    def read_list(self):
        """
        Чтение списка из файла
        """
        list_file = input('Введите имя файла, который хотите открыть: ')
        lst = open('files/{0}'.format(list_file), 'rb')
        r_list = pickle.load(lst)
        print(r_list)
        lst.close()
        sleep(5)

    def write_list(self):
        """
        Запись списка в файл
        """
        list_file = input('Введите имя для сохраняемого списка {0}: '.format(self.t))
        out_list = open('files/{0}'.format(list_file), 'wb')
        if self.t == 'students':
            pickle.dump(self.students, out_list, 2)
        elif self.t == 'teachers':
            pickle.dump(self.teachers, out_list, 2)
        elif self.t == 'other':
            pickle.dump(self.other, out_list, 2)
        out_list.close()
        print('\nФайл сохранен files/{0}'.format(list_file))
        sleep(2)

    def clear_list(self):
        """
        Очистка списка
        """
        q = input('Вы уверены, что хотите очистить список? (Н/д): ').lower()
        if q == 'д' or q == 'y' or q == 'да' or q == 'yes':
            if self.t == 'students':
                self.students.clear()
            elif self.t == 'teachers':
                self.teachers.clear()
            elif self.t == 'other':
                self.other.clear()
            print('Список очищен.')
            sleep(2)  # пауза 2 секунды перед выходм в меню
        else:
            print('Отмена.')
            sleep(2)


if __name__ == '__main__':
    pass
