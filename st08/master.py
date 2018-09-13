from .bachelor import Bachelor


class Master(Bachelor):
    def __init__(self):
        super().read_input()
        self.read_input()


    def read_input(self):
        self.scientific_adviser = input('Научный руководитель: ')

    
    def display(self):
        super().display()
        print('- Научный руководитель: ', self.scientific_adviser)