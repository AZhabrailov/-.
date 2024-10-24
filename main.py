from Customer import *
from Order import *
from menu import *
import sqlite3



db_file1 = "orders.db"
conn = create_connection(db_file)
create_table(conn)
db_file = "customers.db"
exit = 0
while exit != 5:
    what = int(input("\n1. Взаимодействие с посетителем \n2. Взаимодействие с заказом\n3. Взаимодействие с меню\n4. Выход\n"))
    if what == 1:
        exit1 = 0
        while exit1 != 4:
            cl = int(input('\n1.Добавить посетителя\n2.Удалить посетителя\n3.Посмотреть базу посетителей\n4.Выйти\n'))
            if cl == 1:
                name = input('Введите имя посетителя: ')
                amount = input('Введите количетсво человек: ')
                phone = input('Введите номер телефона посетителя: ')
                add_customer(db_file,name,amount,phone)
            elif cl == 2:
                name = input('Введите имя посетителя: ')
                delete_customer(db_file,name)
                print()
            elif cl == 3:
                print_database_info(db_file)
            elif cl == 4:
                exit1 = 4
            else:
                print('Неправильный выбор')
    elif what == 2:
        exit2 = 0
        while exit2 != 4:
            cl = int(input('\n1.Добавить заказ\n2.Удалить заказ\n3.Посмотреть базу заказов\n4.Выйти\n'))
            if cl == 1:
                name = input('Введите имя посетителя: ')
                order_details = input('Введите заказ: ')
                add_order(conn, name, order_details)
            elif cl == 2:
                name = input('Введите имя посетителя: ')
                delete_order(conn, name)
            elif cl == 3:
                get_orders(conn)
            elif cl == 4:
                exit2 = 4
            else:
                print('Неправильный выбор')
    elif what == 3:
        exit3 = 0
        while exit3 != 4:
                cl = int(input('\n1.Добавить блюдо в меню\n2.Удалить блюдо из меню\n3.Посмотреть меню\n4.Добавить позицию в стоп-лист\n5.Проверить позицию в стоп-листе\n6.Удалить позицию из стоп-листа\n7.Выйти\n'))
                if cl == 1:
                    name = input('Введите название блюда: ')
                    order_details = input('Введите описание: ')
                    price = int(input('Введите цену: '))
                    add_dish(name, order_details, price)
                elif cl == 2:
                    name = input('Введите название блюда: ')
                    delete_dish(name)
                elif cl == 3:
                    print_menu()
                elif cl == 4:
                    name = input('Введите название блюда: ')
                    add_to_stop_list(name)
                elif cl == 5:
                    name = input('Введите название блюда: ')
                    check_stop_list(name)
                elif cl == 6:
                    name = input('Введите название блюда: ')
                    remove_from_stop_list(name)
                elif cl == 7:
                    exit3 = 4
                else:
                    print('Неправильный выбор')
    
    else:
        exit = 5



       
        



