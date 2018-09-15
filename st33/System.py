from .Asteroid import Asteroid
from .Planet import Planet
import pickle

class System:
    
    System = []
    File = "st33/system.dat"
    
    def __init__(self):
        pass

    def insert_Asteroid(self):
        NewAsteroid = Asteroid()
        self.System.append(NewAsteroid)
        
    def insert_Planet(self):
        NewPlanet = Planet()
 #       Planet.read_input()
        self.System.append(NewPlanet)
       
    def edit_object(self):
        self.write_system()
        num = input("Номер объекта для редактирования: ")
        self.System[int(num)].read_input()
            
    def delete_object(self):
        self.write_system()
        num = input("Удалить объект №: ")
        del self.System[int(num)]
        print("Объект №: " + num + " удалён")

    def write_system(self):
        if not self.System:
            print("Система не найдена")
        else:
            for i in range(0, len(self.System)):
                print("Система №: ", i + 1)
                self.System[i].write_output()

    def read_from_file(self):
        print("Чтение файла " + System.File)
        file = open(self.File, 'rb')
        self.System = pickle.load(file)
        print("Успешно")
        file.close()
        
    def write_to_file(self):
        print("Запись в " + System.File)
        file = open(self.File, 'wb')
        pickle.dump(self.System, file)
        print("Успешно")
        file.close()

    def clear_system(self):
        self.System.clear()
        print("Успешно")