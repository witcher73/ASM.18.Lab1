class Bachelor:
    def __init__(self):
        self.read_input()


    def read_input(self):
        self.lastname = input('Фамилия: ')
        self.university = input('Университет: ')


    def display(self):
        print('- Фамилия: ', self.lastname)
        print('- Университет: ', self.university)


