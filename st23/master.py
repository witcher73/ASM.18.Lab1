class Master:
    def __init__(self):
        self.read_data()


    def read_data(self):
        while True:
            try:
                self.lastname = input('Фамилия: ')
                self.category = int(input('Категория: '))
                break
            
            except Exception:
                print('Введите цифру')


    def print_data(self):
        print('(Master)\t Фамилия: {0} | Категория: {1}'.format(self.lastname, self.category))