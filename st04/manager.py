from .worker import Worker

class Manager(Worker):
    def read_attributes_from_console(self):
        
        while True:
            try:
                super().read_attributes_from_console()
                
                print('Type salary:')
                self.salary = int(input())

                print('Type work experience:')
                self.work_experience = int(input())
                break
                
            except ValueError:
                print('\nType a number, please\n')


    def print_attributes(self):
        super().print_attributes()
        
        print('Salary: {}'.format(self.salary))
        print('Work experience: {}'.format(self.work_experience))


if __name__ == '__main__':
    manager = Manager()
    manager.read_attributes_from_console()
    manager.print_attributes()