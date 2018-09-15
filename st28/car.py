class Car():
    def __init__(self):
        self.color = None
        self.speed = None
        self.model = None

    @property
    def input(self):
        self.color = input('введите цвет ')
        self.speed = input('введите скорость ')
        self.model = input('введите модель ')
        
    @property
    def print(self):
        print('''
Цвет: {0}
скорость: {1}
модель: {2}
'''.format(self.color, self.speed, self.model))


