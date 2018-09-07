class Worker:
    def read_attributes_from_console(self):
        while True:
            try:
                print('Type name:')
                self.name = input()

                print('Type age:')
                self.age = int(input())
                break
                
            except ValueError:
                print('\nType a number, please\n')


    def print_attributes(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))

    
if __name__ == '__main__':
    w = Worker()
    w.read_attributes_from_console()
    w.print_attributes()