from .car import *

class Supercar(Car):
    def __init__(self):
        super().__init__()
        self.nitro = None
        self.masloradiatory = None

    @property
    def input(self):
        super().input
        self.nitro = input('Введите объем азота: ')
        self.masloradiatory = input('Введите модель маслорадиатора: ')

    @property
    def print(self):
        print('''
Цвет: {0}
скорость: {1}
модель: {2}
Объем азота: {3}
Модель маслорадиатора: {4}
'''.format(self.color,
           self.speed,
           self.model,
           self.nitro,
           self.masloradiatory))
    
        
a = Supercar()
