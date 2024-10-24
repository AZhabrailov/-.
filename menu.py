menu = []
stop_list = []

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Блюдо: {self.name}\nОписание: {self.description}\nЦена: {self.price}"

def add_dish(name, description, price):
    new_dish = Dish(name, description, price)
    menu.append(new_dish)
    print("Блюдо добавлено в меню.")

def remove_dish(name):
    for dish in menu:
        if dish.name == name:
            menu.remove(dish)
            print(f"Блюдо '{name}' удалено из меню.")
            return
    print(f"Блюда с названием '{name}' не найдено.")

def add_to_stop_list(name):
    for dish in menu:
        if dish.name == name:
            stop_list.append(dish)
            menu.remove(dish)
            print(f"Блюдо '{name}' добавлено в стоп-лист.")
            return
    print(f"Блюда с названием '{name}' не найдено.")

def remove_from_stop_list(name):
    for dish in stop_list:
        if dish.name == name:
            stop_list.remove(dish)
            menu.append(dish)
            print(f"Блюдо '{name}' удалено из стоп-листа.")
            return
    print(f"Блюда с названием '{name}' не найдено в стоп-листе.")

def print_menu():
    if not menu:
        print("Меню пусто.")
    else:
        for dish in menu:
            print(dish)


def check_stop_list(name):
    if any(dish.name == name for dish in stop_list):
            print(f"Блюдо '{name}' находится в стоп-листе.")
            return
    else:
        print(f"Блюдо '{name}' не находится в стоп-листе.")
        return
# Пример использования
add_dish("Борщ", "Классический украинский борщ", 150)
add_dish("Плов", "Восточное блюдо из риса и мяса", 200)
