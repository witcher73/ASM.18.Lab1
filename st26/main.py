# -*- coding: utf-8 -*-

from time import sleep
from os import system
from container import Container


def main_menu():
    """
    Функция основного меню
    """
    # основное меню
    main_menu_list = """
    1. Добавить новый объект.
    2. Вывести список.
    3. Очистить список.
    4. Записать список в файл.
    5. Прочитать список из файла.
    0. Вернуться назад.
    00.Выход.
    """
    # меню выбора списка
    menu_type = """
    1.Список студентов.
    2.Список преподавателей.
    3.Список работников универа.
    0.Выход.
    """
    # варианты выбора в меню списков
    menu_type_ans = {
            '1': 'students',
            '2': 'teachers',
            '3': 'other'
            }
    system('clear')     # очистка консоли
    print(menu_type)    # вывод меню
    ans = input('Выберите пункт: ')
    if ans == '0':
        exit(0)
    # вызов методов из основного меню
    try:
        main_menu_ans = {
                '1': Container('{0}'.format(menu_type_ans['{0}'.format(ans)])).add_list,
                '2': Container('{0}'.format(menu_type_ans['{0}'.format(ans)])).get_list,
                '3': Container('{0}'.format(menu_type_ans['{0}'.format(ans)])).clear_list,
                '4': Container('{0}'.format(menu_type_ans['{0}'.format(ans)])).write_list,
                '5': Container('{0}'.format(menu_type_ans['{0}'.format(ans)])).read_list,
                '0': main_menu
                }
    except KeyError:
        print('Ошибка. Попробуйте еще раз.')
        sleep(2)
        main_menu()
    system('clear')
    print(main_menu_list)
    ans1 = input('Выберите пункт: ')
    if ans1 == '00':
        exit(0)
    system('clear')
    try:
        main_menu_ans['{0}'.format(ans1)]()   # вызов методфа, выбранного в меню
    except KeyError:
        print('Ошибка. Попробуйте еще раз.')
        sleep(2)
        main_menu()
    main_menu()    # возврат в меню после завершения выполнения функции


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print('\nВыход.')
        exit(0)
