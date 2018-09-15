class Asteroid:
    def __init__(self):
        self.read_input()
        
    def read_input(self):
        self.Name = input("Название: ")
        self.Weight = input("Масса: ")
        self.Diameter = input("Диаметр: ")
        self.Class = input("Класс: ")
        self.Yr_of_dis = input("Год открытия: ")
        
    def write_output(self):
        print("Название: " + self.Name)
        print("Масса: " + self.Weight)
        print("Диаметр: " + self.Diameter)
        print("Класс: " + self.Class)
        print("Год открытия: " + self.Yr_of_dis)