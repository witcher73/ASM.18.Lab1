import pickle

from .bachelor import Bachelor
from .master import Master


class University:

    FILENAME = 'st08/dump'

    def __init__(self):
        self.people = []


    def add_bachelor(self):
        b = Bachelor()
        self.people.append(b)


    def add_master(self):
        m = Master()
        self.people.append(m)


    def print_people(self):
        if len(self.people) == 0:
            print('Никого нет')
            return

        print('------------------------------')
        for p in self.people:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')


    def edit_people(self):
        if len(self.people) == 0:
            print('Никого нет')
            return

        print('Число студентов: ', len(self.people))

        try:    
            ind = int(input('Индекс студента (0 вернуться назад): '))

            if ind == 0:
                return

            self.people[ind - 1].read_input()
        except Exception as ex:
            print(ex)
            print('А ты любопытный')


    def save_to_file(self):
        with open(self.FILENAME, 'wb') as f:
            pickle.dump(self.people, f, -1)
            print('Данные сохранены')


    def load_from_file(self):
        try:
            with open(self.FILENAME, 'rb') as f:
                self.people = pickle.load(f)

            print('Загрузка выполнена')
        
        except FileNotFoundError:
            print('Не нашелся файл')


    def delete_from_people(self):
        if len(self.people) == 0:
            print('Никого нет')
            return

        print('Число студентов: ', len(self.people))
        
        try:
            ind = int(input('Индекс студента (0 вернуться назад): '))

            if ind == 0:
                return

            del self.people[ind - 1]
            print('Удаление прошло успешно')
        
        except Exception as ex:
            print(ex)
            print('А ты любопытный')

    
    def clear_people(self):
        self.people = []