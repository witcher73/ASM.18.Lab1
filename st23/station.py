import pickle

from .master import Master
from .engineer import Engineer


class Station:
    def __init__(self):
        self.__staff = []
        self.__filename = 'st23/data'


    def add_master(self):
        self.__staff.append(Master())


    def add_engineer(self):
        self.__staff.append(Engineer())


    def edit_staff(self):
        if not self.__staff:
            print('Штат пуст')
            return

        print('Число людей в штате: {}'.format(len(self.__staff)))
        
        try:
            index_to_edit = int(input('ID человека (0 вернуться назад): '))

            if index_to_edit == 0:
                return

            self.__staff[index_to_edit - 1].read_data()
            print('Изменения внесены')
        
        except Exception:
            print('Ошибка')


    def print_staff(self):
        if not self.__staff:
            print('Штат пуст')
            return

        for item in self.__staff:
            item.print_data()


    def save_to_file(self):
        with open(self.__filename, 'wb') as f:
            pickle.dump(self.__staff, f, -1)
            print('Сохранено')


    def load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f:
                self.__staff = pickle.load(f)

            print('Загружено')
        
        except FileNotFoundError:
            print('Файл не существует')


    def delete_people(self):
        if not self.__staff:
            print('Штат пуст')
            return

        print('Число людей в штате: {}'.format(len(self.__staff)))
        
        try:
            index_to_edit = int(input('ID человека (0 вернуться назад): '))

            if index_to_edit == 0:
                return

            del self.__staff[index_to_edit - 1]
            print('Изменения внесены')
        
        except Exception:
            print('Ошибка')


    def clear_staff(self):
        self.__staff = []
        