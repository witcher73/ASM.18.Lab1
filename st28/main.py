from .container import *

def main():
    c = Container()
    while True:
        choice = input('''
    1 - добавить обычную машину
    2 - добавить суперкар
    3 - редактировать выбранную машину
    4 - удалить выбранную машину
    5 - удалить все
    6 - записать в файл
    7 - считать с файла
    8 - вывести список
    ''')
        
        if choice == '1':
            c.add_car
        elif choice == '2':
            c.add_supercar
        elif choice == '3':
            c.edit
        elif choice == '4':
            c.delete
        elif choice == '5':
            c.clear_container
        elif choice == '6':
            c.write_in_file
        elif choice == '7':
            c.read_from_file
        elif choice == '8':
            c.show



if __name__ == '__main__':
	main()
