from .university import University

u = University()

MENU = [
    ('Добавить бакалавра', u.add_bachelor),
    ('Добавить магистра', u.add_master),
    ('Изменить данные по студенту', u.edit_people),
    ('Вывести всех студентов', u.print_people),
    ('Сохранить в файл', u.save_to_file),
    ('Загрузить из файла', u.load_from_file),
    ('Удалить студента', u.delete_from_people),
    ('Очистить всех', u.clear_people)
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
            print('А ты любопытный')