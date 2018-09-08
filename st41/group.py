from .person import Person
from .student import Student
import pickle 

class Group:
    
    FILE_NAME = "st41/backup"
    
    def __init__(self):
        self.__peoples = []
    
    def addPerson(self):
        self.__peoples.append(Person())
        
    def addStudent(self):
        self.__peoples.append(Student())
        
    def print(self):
        print("There are", len(self.__peoples), "peoples:")
        i = 1
        for p in self.__peoples:
            print("____")
            print("№" + str(i))
            p.print()
            print("____")
            i += 1
    
    def __checkRange(self, i):
        if i < 0 or i >= len(self.__peoples):
            raise IndexError("Out of range")
    
    def edit(self, i):
        self.__checkRange(i)
        self.__peoples[i].read() 
        
    def remove(self, i):
        self.__checkRange(i)
        del self.__peoples[i]
            
    def clear(self):
        self.__peoples.clear()
        
    def saveToFile(self):
        with open(self.FILE_NAME, "wb") as f:
            pickle.dump(self.__peoples, f)
            
    def loadFromFile(self):
        with open(self.FILE_NAME, "rb") as f:
            self.__peoples = pickle.load(f)
        