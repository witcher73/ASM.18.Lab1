from .supercar import *
import pickle

FILENAME = '28.txt'

class Container():
    
    def __init__(self):
        self.container = []

    @property
    def add_car(self):
        car = Car()
        car.input
        self.container.append(car)

    @property
    def add_supercar(self):
        car = Supercar()
        car.input
        self.container.append(car)

    @property
    def edit(self):
        car_number = int(input('введите номер редактируемой машины в списке'))
        self.container[car_number].input

    @property
    def delete(self):
        car_number = int(input('введите номер удаляемой машины в списке'))
        self.container.pop(car_number)

    @property
    def clear_container(self):
        answer = input('Вы действительно хотите все удалить?(да/нет)')
        if answer == 'да':
            self.container.clear()

    @property
    def show(self):
        for car in self.container:
            car.print
                       
    @property
    def write_in_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.container, file)

    @property
    def read_from_file(self):
        with open(FILENAME, 'rb') as file:
            self.container += pickle.load(file)

a =  Container()
                       
            
        
