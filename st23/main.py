from .station import Station


station = Station()

MENU = [
    ('Добавить мастера', station.add_master),
    ('Добавить инженера', station.add_engineer),
    ('Просмотр штата', station.print_staff),
    ('Изменить', station.edit_staff),
    ('Сохранить в файл', station.save_to_file),
    ('Загрузить из файла', station.load_from_file),
    ('Удалить', station.delete_people),
    ('Очистить', station.clear_staff)
]


def print_menu():
    print('----------------------')
    for i, item in enumerate(MENU, start=1):
        print('{0}: {1}'.format(i, item[0]))
    print('----------------------')


def main():
    while True:
        print_menu()

        try:
            choice = int(input('>> '))

            if choice == 0:
                break

            MENU[choice - 1][1]()
        
        except Exception:
            print('Ошибка')
