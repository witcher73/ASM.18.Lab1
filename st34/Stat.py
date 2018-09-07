from .Character import Character

class Stat(Character):


    def __init__(self):
        super().__init__()
        self.Health = []
        self.Haste = []

         
    def input(self):
        self.Health = input("Health:")
        self.Haste = input("Haste:")


    def output(self):
        print("\nHealth:" + self.Health + "\nHaste:" + self.Haste)
