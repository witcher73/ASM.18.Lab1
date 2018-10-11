from .army import Army

army = Army()

MENU = [
    ('Добавить солдата', army.add_soldier),
    ('Добавить офицера', army.add_officer),
    ('Изменить данные по военнослужащему', army.edit_serviceman),
    ('Вывести всех военнослужащих', army.print_serviceman),
    ('Сохранить в файл', army.save_to_file),
    ('Загрузить из файла', army.load_from_file),
    ('Удалить военнослужащего', army.delete_from_serviceman),
    ('Очистить всех', army.clear_serviceman)
]


def main():

    while True:
        print('------------------------------')
        for i, item in enumerate(MENU, start=1):
            print('{0}: {1}'.format(i, item[0]))
        print('------------------------------')


        try:
            choice = int(input('>> '))

            if choice == 0:
                break

            MENU[choice - 1][1]()
        
        except Exception as ex:
            print(ex)
            print('Не пойдет')