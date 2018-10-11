import pickle

from .soldier import Soldier
from .officer import Officer


class Army:

    FILENAME = 'st35/dump'

    def __init__(self):
        self.serviceman = []


    def add_bachelor(self):
        s = Soldier()
        self.serviceman.append(s)


    def add_master(self):
        o = Officer()
        self.serviceman.append(o)


    def print_serviceman(self):
        if len(self.serviceman) == 0:
            print('Ни душы')
            return

        print('------------------------------')
        for p in self.serviceman:
            print('\t', p.__class__.__name__)
            p.display()
            print('------------------------------')


    def edit_serviceman(self):
        if len(self.serviceman) == 0:
            print('Никого нет')
            return

        print('Число военнослужащих: ', len(self.serviceman))

        try:    
            ind = int(input('Индекс военнослужащего (0 вернуться назад): '))

            if ind == 0:
                return

            self.serviceman[ind - 1].read_input()
        except Exception as ex:
            print(ex)
            print('Не пойдет')


    def save_to_file(self):
        with open(self.FILENAME, 'wb') as f:
            pickle.dump(self.serviceman, f, -1)
            print('Сохранено успешно')


    def load_from_file(self):
        try:
            with open(self.FILENAME, 'rb') as f:
                self.serviceman = pickle.load(f)

            print('Загружено')
        
        except FileNotFoundError:
            print('Отсутствует файл')


    def delete_from_serviceman(self):
        if len(self.serviceman) == 0:
            print('Ни душы')
            return

        print('Число военнослужащих: ', len(self.serviceman))
        
        try:
            ind = int(input('Индекс военнослужащего (0 вернуться назад): '))

            if ind == 0:
                return

            del self.serviceman[ind - 1]
            print('Чистка завершена')
        
        except Exception as ex:
            print(ex)
            print('Не пойдет')

    
    def clear_serviceman(self):
        self.serviceman = []