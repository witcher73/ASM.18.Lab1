class Soldier:
    def __init__(self):
        self.read_input()


    def read_input(self):
        self.lastname = input('Фамилия: ')
        self.army = input('Военная часть: ')


    def display(self):
        print('- Фамилия: ', self.lastname)
        print('- Военная часть: ', self.army)


