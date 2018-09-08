class Person:
    
    def __init__(self):
        self.read()
       
    def read(self):
        self.__name = input("Name: ")
        self.__age = int(input("Age: "))
        
    def print(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        