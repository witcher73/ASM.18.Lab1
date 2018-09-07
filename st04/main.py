import company


def add_worker(some_company: object):
    while True:
        print('\nChoose type of worker:')
        print('1 - Base worker')
        print('2 - Manager')
        print('0 - Back to main menu')

        try:
            variable = int(input())

            if variable == 0:
                break

            if variable == 1:
                some_company.add_worker()
                break

            if variable == 2:
                some_company.add_manager()
                break

        except ValueError:
            print('\nType a number, please')


def edit_worker(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty')
        return

    print('\nChoose ID of worker to edit in [{0}, {1}]:'.format(0, len(some_company.storage) - 1))

    try:
        variable = int(input())

        if variable in range(len(some_company.storage)):
            print(some_company.storage[variable])
            some_company.storage[variable].read_attributes_from_console()
        else:
            print('No ID found')
    
    except ValueError:
        print('\nType a number, please')
            

def delete_worker(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty')
        return

    print('\nChoose ID worker to delete in [{0}, {1}]:'.format(0, len(some_company.storage) - 1))
    
    try:
        variable = int(input())

        if variable in range(len(some_company.storage)):
            some_company.delete_worker_by_index(variable)
        else:
            print('No ID found')

    except ValueError:
        print('\nType a number, please')


def print_storage(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty\n')
        return
    
    some_company.print_storage()


def save_to_file(some_company: object):
    if len(some_company.storage) == 0:
        print('\nStorage is empty\n')
        return

    some_company.write_to_file()


def load_from_file(some_company: object):
    some_company.load_from_file()


def erase_storage(some_company: object):
    some_company.clean_storage()


def menu():
    some_company = company.Company()
    
    choice = {
        1: add_worker,
        2: edit_worker,
        3: delete_worker,
        4: print_storage, 
        5: save_to_file,
        6: load_from_file,
        7: erase_storage
    }
    
    while True:
        print('\n------MENU------')
        print('1 - Add worker')
        print('2 - Edit worker')
        print('3 - Delete worker') 
        print('4 - Print all storage')
        print('5 - Save to file')
        print('6 - Load from file')
        print('7 - Erase storage')
        print('0 - Exit')

        try:
            variable = int(input())

            if variable == 0:
                break

            if variable in range(len(choice) + 1):
                choice[variable](some_company)
        except ValueError:
            print('\nType a number, please')


if __name__ == '__main__':
    menu()