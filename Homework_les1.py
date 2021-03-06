__author__ = 'Степованый Владислав Геннадьевич'
"""EASY"""
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Задача-1 :

import random
a=random.randint(0,999999)
i = 0
a = str(a)
while i <= len(a):
    num = int(a[i])
    print(num)
    i = i+1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# Задача-2 :

a = input("Введите число a")
b = input("Введите число b")
c = a
a = b
b = c
print ("Число а приняло значение = "+a)
print ("Число b приняло значение = "+b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Задача-3 :

a = int (input("Введите Ваш возраст"))
if a >= 18:
    print ("Доступ разрешен!")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет!")

"""NORMAL"""

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Задача-1 :

import random
a=random.randint(0,999999)
i = 0
a = str(a)
c = 0
for i in range(0, len(a)):
    num = int(a[i])
    if num >= c:
        c = num
    i = i+1
print (c)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


a = int (input("Введите число a"))
b = int (input("Введите число b"))
a = a + b
b = a - b
a = a - b
a = str (a)
b = str (b)
print ("Число а приняло значение = "+a)
print ("Число b приняло значение = "+b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# Задача-3 :

import math
a = int (input("Введите число a"))
b = int (input("Введите число b"))
c = int (input("Введите число c"))
x_1 = 0
x_2 = 0
D = b**2-4*a*c
if D>0:
    x_1=(-b+math.sqrt(D))/(2*a)
    x_1 = str (x_1)
    print ("x1 = "+x_1)
    x_2 = (-b - math.sqrt(D)) / (2 * a)
    x_2 = str(x_2)
    print("x2 = " + x_2)
elif D==0:
    x_1=(-b+math.sqrt(D))/(2*a)
    x_1 = str (x_1)
    print ("x = "+x_1)
else:
    print ("Корней нет!")
