from .Asteroid import Asteroid

class Planet(Asteroid):
    def __init__(self):
        self.read_input()
        
    def read_input(self):
        Asteroid.read_input(self)
        self.habitable = input("Обитаема: ")
        self.satellites = input("Количество спутников: ")
        
    def write_output(self):
        print("Название: " + self.Name)
        print("Масса: " + self.Weight)
        print("Диаметр: " + self.Diameter)
        print("Класс: " + self.Class)
        print("Год открытия: " + self.Yr_of_dis)
        print("Обитаема: " + self.habitable)
        print("Количество спутников: " + self.satellites)