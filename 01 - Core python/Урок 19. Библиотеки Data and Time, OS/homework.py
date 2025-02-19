# Тема: Модуль datetime
import datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45

now = datetime.datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_now)

# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

from datetime import datetime
def give_birthday():
    print("Когда твой день рождения?")
    birthday =input()
    date_object = datetime.strptime(birthday, "%Y-%m-%d")
    return date_object
def how_old(date_object):
    old_year = datetime.now().year - date_object.year
    if datetime.now().month < date_object.month or (datetime.now().month == date_object.month and datetime.now().day < date_object.day):
     old_year -= 1
    print(old_year)
result = give_birthday()
how_old(result)

# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.
dt = input("Введи дату мероприятия")
dt = datetime.strptime(dt, "%Y-%m-%d")
now = datetime.now()
date = dt - now
result = date.days
print(result)

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

date = input("Enter date in format 'YYYY-MM-DD': ")
date = datetime.strptime(date, "%Y-%m-%d")
print(date.strftime("%A"))

# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.

dt_1 = input("Введи первую дату: ")
dt_2 = input("Введи вторую дату: ")
dt_1 = datetime.strptime(dt_1, "%Y-%m-%d")
dt_2 = datetime.strptime(dt_2, "%Y-%m-%d")
if dt_1 > dt_2:
    print("Первая дата позже")
elif dt_1 < dt_2:
    print("Вторая дата позже")
else:
    print("Даты равны")

# Тема: Модуль os
import os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.
os.mkdir('test_directory')
current_directory = os.getcwd()
print(current_directory)

files_and_directories = os.listdir('/Users/igorjahn/PycharmProjects/starta/g160125-m-pt/01 - Core python/Урок 19. Библиотеки Data and Time, OS')
print(files_and_directories)  # Вывод: ['file1.txt', 'file2.txt', 'directory1']
os.rmdir('test_directory')

# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.

with open ("temp_file.txt", "w") as file:
    file.write("Temporary content")
os.rename("temp_file.txt", "renamed.txt")
print(os.listdir("."))

# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".
exists = os.path.exists("example.txt")
print(exists)
if exists == True:
    info = os.stat("example.txt")
    print(info)
else:
    print("File not found")

# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".

with open("example.txt", "w") as file:
    file.write("Hello, World")
exists = os.path.exists('example.txt')
print(exists)
if exists == True:
    info = os.stat('example.txt')
    print(info.st_size)
else:
    print("Файл не найден")

info2 = os.stat("renamed.txt")
print(info2.st_size)

if info2.st_size > info.st_size:
    print("Renamed bigger than example")
else:
    print("Renamed smaller than example")

# Тема: Интеграционная практика.

# Проект: Перепишите проект из уроков 7-8, 14-15, добавив в него фичи 1 - 3 на основе модулей datetime и os.
#
# Фича 1. Добавьте в каждый товар дату и время его создания,
# а также дату и время обновления данных о товаре или количества товара.
#
# Фича 2: Логирование действий с товарами
# Создайте лог-файл, куда будет записываться история всех действий с товарами (добавление, удаление, обновление).
# Используйте модуль datetime для добавления временных меток к каждому действию с товарами.
#
# Фича 3. Резервное копирование данных:
# Используйте модуль os для создания резервных копий файла с товарами.
# Например, при каждом запуске программы создается копия файла с добавлением текущей даты и времени.
#
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
# Используйте файл как базу данных проекта.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.

import time
from datetime import datetime
from json import JSONDecodeError
map_count_call = {}
DB = 'inventory.json'
DB_COPY = 'inventory_copy.json'
def retry_on_error(func):
    global map_count_call
    if func.__name__ not in map_count_call:
        map_count_call[func.__name__] = 0
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (FileNotFoundError, IOError, JSONDecodeError) as e:
            time.sleep(10)
        except Exception as e:
            print(f"Ошибка: {e}")
            map_count_call[func.__name__] += 1
            if map_count_call[func.__name__] == 3:
                print(f"Превышено количество попыток вызова функции {func.__name__}")
                exit(1)
            return wrapper(*args, **kwargs)
        else:
            map_count_call[func.__name__] = 0
    return wrapper

def log_it(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as file:
            file.write(f"{datetime.now()} Вызвана функция {func.__name__}. Результат: {result}\n")
        return result
    return wrapper

@retry_on_error
def save_inventory(inventory):
    with open(DB, 'w') as file:
        for el in inventory:
            if 'created_at' in el:
                el['created_at'] = el['created_at'].isoformat()
            else:
                el['created_at'] = datetime.now().isoformat()
        json.dump(inventory, file)

@retry_on_error
def load_inventory():
    # try:1
    with open(DB) as file:
        data = json.load(file)
        for el in data:
            if 'created_at' in el:
                el['created_at'] = datetime.fromisoformat(el['created_at'])
            else:
                el['created_at'] = datetime.now()
        return data
    # except (FileNotFoundError, IOError, JSONDecodeError) as e:
    #     print(f"Ошибка: {e}")
    #     return []


def show_inventory(inventory):
    for product in inventory:
        print_product(product)
@log_it
def add_product(inventory):
    product = input("Enter product name: ")
    try:
        price = int(input("Enter product price: "))
        count = int(input("Enter product count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return add_product(inventory)
    inventory.append({'product': product.title(), 'price': price, 'count': count, "created_at": datetime.now()})
    return inventory
@log_it
def remove_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            inventory.remove(item)
    return inventory
@log_it
def edit_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            try:
                new_product = input(f"Enter new product name or {item['product']}: ")
                if new_product:
                    item['product'] = new_product.title()
                new_price = input(f"Enter new product price or {item['price']}: ")
                if new_price:
                    item['price'] = int(new_price) * 0.1
                new_count = input(f"Enter new product count or {item['count']}: ")
                if new_count:
                    item['count'] = int(new_count)
            except ValueError as e:
                print(f"Ошибка: {e}")
                return edit_product(inventory)
    return inventory

def find_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            print_product(item)

def find_product_min_cost(inventory):
    try:
        price = int(input("Enter price: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return find_product_min_cost(inventory)
    for item in inventory:
        if item['price'] <= price:
            print_product(item)

def print_product(product):
    print(f"Product: {product['product']} Price: {product['price']} Count: {product['count']} Created at: {product['created_at']}")

def find_product_min_count(inventory):
    try:
        count = int(input("Enter count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return find_product_min_count(inventory)
    for item in inventory:
        if item['count'] <= count:
            print_product(item)

def copy_file(origin_path, new_path):
    def read_file_by_cunck(file, size=1024):
        while True:
            data = file.read(size)
            if not data:
                break
            yield data
    def write_file_by_cunck(file, data):
        for chunk in data:
            file.write(chunk)
    for el in read_file_by_cunck(open(origin_path, 'rb')):
        with open(new_path, 'wb') as file:
            write_file_by_cunck(file, el)


while True:
    inventory = load_inventory()
    user_input = input(
        "1. Показать список товаров.\n"
        "2. Добавить товар.\n"
        "3. Удалить товар.\n"
        "4. Обновить название товара, стоимость или количество.\n"
        "5. Найти товар по названию.\n"
        "6. Вывести список товаров меньше определнной стоимости.\n"
        "7. Вывести список товаров меньше определенного количества.\n"
        "8. Выйти.\n"
    )
    match user_input:
        case "1":
            show_inventory(inventory)
        case "2":
            inventory = add_product(inventory)
            save_inventory(inventory)
        case "3":
            inventory = remove_product(inventory)
            save_inventory(inventory)
        case "4":
            inventory = edit_product(inventory)
            save_inventory(inventory)
        case "5":
            find_product(inventory)
        case "6":
            find_product_min_cost(inventory)
        case "7":
            find_product_min_count(inventory)
        case "8":
            if os.path.exists(DB_COPY):
                os.unlink(DB_COPY)
            with open(DB, 'r') as file:
                with open(DB_COPY, 'w') as file_copy:
                    file_copy.write(file.read())
            break
        case _:
            print("Invalid input")











