from .person import Person

class Student(Person):
    
    def __init__(self):
        self.read()
               
    def read(self):
        Person.read(self)
        self.__course = int(input("Course: "))
        self.__faculty = input("Faculty: ")
        
    def print(self):
        Person.print(self)
        print("Course: ", self.__course)
        print("Faculty: ", self.__faculty)