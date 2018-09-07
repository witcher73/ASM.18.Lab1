class Character:
    
    
    def __init__(self):
         self.name = []
         self.klas = []
         self.specialization = []


    def input(self):
        self.name = input("Name:")
        self.klas = input("Klas:")
        self.specialization = input("Specialization:")
    
    
    def output(self):
        print("Name:" + self.name + "\nKlas:" + self.klas + "\nSpecialization:" + self.specialization )

