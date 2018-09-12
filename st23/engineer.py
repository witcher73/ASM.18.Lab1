from .master import Master


class Engineer(Master):
    def __init__(self):
        super().read_data()
        self.read_data()

    def read_data(self):
        while True:
            try:
                self.numEducations = int(input('Количество образований: '))
                self.rank = int(input('Разряд: '))
                break
            
            except ValueError:
                print('Введите цифру')


    def print_data(self):
        print('(Engineer)\t Фамилия: {0} | Категория: {1} | Количество образований: {2} | Разряд: {3}'.format(
            self.lastname, self.category, self.numEducations, self.rank))