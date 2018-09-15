from .System import System

system = System()

menu = {
    "1": ("Добавить астероид", system.insert_Asteroid),
    "2": ("Добавить планету", system.insert_Planet),
    "3": ("Удалить объект", system.delete_object),
    "4": ("Изменить объект", system.edit_object),
    "5": ("Вывод системы на экран", system.write_system),
    "6": ("Запись в файл", system.write_to_file),
    "7": ("Чтение из файла", system.read_from_file),
    "8": ("Очистить систему", system.clear_system),
    "9": ("Выход", None) }

def main():
    while True:
        for i in menu:
            print(i, ": ", menu[i][0])
        k = input("Номер команды: ")
        if k.isdigit():
            if int(k) <= len(menu):
                if int(k) == 9:
                    break
                else:
                    menu[k][1]()
            else:
                print("Номер не соответствует заданной границе")
        else:
            print("Вы должны ввести число!")


if __name__ == "__main__":
    main()