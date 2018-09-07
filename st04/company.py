import pickle

from .worker import Worker
from .manager import Manager


class Company():
    
    def __init__(self):
        self.storage = []


    def add_worker(self):
        w = Worker()
        w.read_attributes_from_console()
        self.storage.append(w)


    def add_manager(self):
        m = Manager()
        m.read_attributes_from_console()
        self.storage.append(m)


    def print_storage(self):       
        for i, worker in enumerate(self.storage):
            print('\nWorker #{}'.format(i))
            print('--------------------')
            worker.print_attributes()


    def write_to_file(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.storage, f)


    def load_from_file(self):
        try:
            with open('data.pickle', 'rb') as f:
                self.storage = pickle.load(f)
        
        except FileNotFoundError:
            print('\nFile does not exist')


    def delete_worker_by_index(self, index: int):
        del self.storage[index]


    def clean_storage(self):
        del self.storage[:]


if __name__ == '__main__':
    company = Company()
    #company.add_worker()
    #company.add_manager()
    #company.print_storage()

    #print('Clear')
    #company.clean_storage()
    #company.print_storage()

    #company.write_to_file()
    company.load_from_file()
    company.print_storage()