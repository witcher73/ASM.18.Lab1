from .soldier import Soldier


class Officer(Soldier):
    def __init__(self):
        super().read_input()
        self.read_input()


    def read_input(self):
        self.direct_superior = input('Непосредственный начальник: ')

    
    def display(self):
        super().display()
        print('- Непосредственный начальник: ', self.direct_superior)