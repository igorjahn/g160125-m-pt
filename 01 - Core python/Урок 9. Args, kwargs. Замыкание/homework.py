# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5,6))

# 2. Напишите функцию combine_lists, которая принимает
# несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
lists = (
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
)
def combine_lists(*args):
    new_list = []
    for list_ in args:
        new_list.extend(list_)
    return new_list
print(combine_lists(*lists))





# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age,
# распакуйте его и передайте в функцию print_details.

def print_details(name, age):
    print(name, age)
    return persons
persons = {"name": "Alice", "age": 30}
print_details(**persons)
print(print_details(**persons))



# 4. Напишите функцию filter_numbers,
# которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.


def filter_numbers(*args):
    more10_numbers = []
    less10_numbers =[]
    for num in args:
        if num >= 10:
            more10_numbers.append(num)
        else:
            less10_numbers.append(num)
    return more10_numbers, less10_numbers
numbers_tuple = (1,4,5,10,12,15)
print(filter_numbers(*numbers_tuple))
# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global,
# которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.

# counter = 0
# def increment_global():
#     global counter
#     counter+=1
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2


# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner.
# Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции,
# на 1 каждый раз при её вызове.

def outer():
    counter = 0

    def inner():
        nonlocal counter
        counter+=1
        return counter
    return inner
counter = outer()
print(counter())  # Вывод: 1
print(counter())  # Вывод: 2


# 3. Напишите функцию make_multiplier,
# которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.

def make_multiplier(factor):
    def multiplier(num):
        return num * factor
    return multiplier
mult_by_2 = make_multiplier(2)
print(mult_by_2(5))  # Вывод: 10
mult_by_3 = make_multiplier(3)
print(mult_by_3(5))  # Вывод: 15
mult_by_4 = make_multiplier(4)
print(mult_by_4(5))

# 4. Напишите функцию make_prefixer,
# которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.


def make_prefixer(prefix):
    def prefixer(num):
        return f'{prefix} {num}'
    return prefixer
add_hello = make_prefixer("Hello, ")
print(add_hello("Alice"))  # Вывод: Hello, Alice
print(add_hello("Bob"))    # Вывод: Hello, Bob



# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple


# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!


# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world


# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor