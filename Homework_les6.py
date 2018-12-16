__author__ = 'Степованый Владислав Геннадьевич'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

def my_round(number, ndigits):  #функция округления с предыдущих дз
    number = number * (10**ndigits) + 0.41
    number = number // 1
    return number / (10**ndigits)

class Triangle():
    def __init__(self, a1_x, a1_y, a2_x, a2_y, a3_x, a3_y):
        self.x_1 = int(a1_x)
        self.x_2 = int(a2_x)
        self.x_3 = int(a3_x)
        self.y_1 = int(a1_y)
        self.y_2 = int(a2_y)
        self.y_3 = int(a3_y)
        print("Треугольник существует!")

    def Perimeter(self):
        AB = math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)
        BC = math.sqrt((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2)
        AC = math.sqrt((self.x_3 - self.x_1) ** 2 + (self.y_3 - self.y_1) ** 2)
        P = AB + BC + AC
        P = my_round(P, 2)
        return P

    def Area(self):
        b = (self.x_1 - self.x_3) * (self.y_1 - self.y_3) - (self.x_2 - self.x_3) * (self.y_2 - self.y_3)
        S = 1/2 * math.fabs(b)
        return S

    def Height(self):
        b = (self.x_1 - self.x_3) * (self.y_1 - self.y_3) - (self.x_2 - self.x_3) * (self.y_2 - self.y_3)
        S = 1 / 2 * math.fabs(b)
        hAB = math.fabs(2 * S / math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2))
        hAB = my_round(hAB, 2)
        hBC = math.fabs(2 * S / math.sqrt((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2))
        hBC = my_round(hBC, 2)
        hAC = math.fabs(2 * S / math.sqrt((self.x_3 - self.x_1) ** 2 + (self.y_3 - self.y_1) ** 2))
        hAC = my_round(hAC, 2)
        return hAB, hBC, hAC



K = Triangle(1, 1, 1, 6, 5, 2)
print(K.Area())
print(K.Perimeter())
print(K.Height())
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium():
    def __init__(self, a1_x, a1_y, a2_x, a2_y, a3_x, a3_y, a4_x, a4_y):
        self.x_1 = int(a1_x)
        self.x_2 = int(a2_x)
        self.x_3 = int(a3_x)
        self.x_4 = int(a4_x)
        self.y_1 = int(a1_y)
        self.y_2 = int(a2_y)
        self.y_3 = int(a3_y)
        self.y_4 = int(a4_y)
        print("Трaпеция существует!")

    def CheckEqualSides(self):
        q = 0
        if self.y_1 == self.y_4:
            q += 1
        if self.y_3 == self.y_4:
            q += 1
        if self.y_2 == self.y_3:
            q += 1
        if self.y_1 == self.y_2:
            q += 1
        if self.x_1 == self.x_4:
            q += 1
        if self.x_3 == self.x_4:
            q += 1
        if self.x_2 == self.x_3:
            q += 1
        if self.x_1 == self.x_2:
            q += 1
        if q == 2:
            return True
        else:
            return False

    def Lenght(self):
        AB = math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)
        BC = math.sqrt((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2)
        CD = math.sqrt((self.x_4 - self.x_3) ** 2 + (self.y_4 - self.y_3) ** 2)
        AD = math.sqrt((self.x_4 - self.x_1) ** 2 + (self.y_4 - self.y_1) ** 2)
        AB = my_round(AB, 2)
        BC = my_round(BC, 2)
        CD = my_round(CD, 2)
        AD = my_round(AD, 2)
        return AB, BC, CD, AD

    def Perimetr(self):
        AB = math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)
        BC = math.sqrt((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2)
        CD = math.sqrt((self.x_4 - self.x_3) ** 2 + (self.y_4 - self.y_3) ** 2)
        AD = math.sqrt((self.x_4 - self.x_1) ** 2 + (self.y_4 - self.y_1) ** 2)
        P = AB + BC + CD + AD
        P = my_round(P, 2)
        return P

    def Area(self):
        AB = math.sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)
        BC = math.sqrt((self.x_3 - self.x_2) ** 2 + (self.y_3 - self.y_2) ** 2)
        CD = math.sqrt((self.x_4 - self.x_3) ** 2 + (self.y_4 - self.y_3) ** 2)
        AD = math.sqrt((self.x_4 - self.x_1) ** 2 + (self.y_4 - self.y_1) ** 2)
        if AB == CD:
            S = 1/2 * (self.y_2 - self.y_1) * (BC + AD)
            S = my_round(S, 2)
            return S
        elif BC == AD:
            S = 1 / 2 * (self.y_3 - self.y_2) * (AB + CD)
            S = my_round(S, 2)
            return S
        else:
            return "Это не равнобедренная трапеция"


J = Trapezium(1, 1, 2, 4, 7, 4, 8, 1)
print(J.CheckEqualSides())
print(J.Lenght())
print(J.Perimetr())
print(J.Area())

"""NORMAL"""

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random
class People:
    def __init__(self, name):
        self.name = name


class Student(People):
    def __init__(self, name, mum, dad, klass):
        People.__init__(self, name)
        self.mum = mum
        self.dad = dad
        self.klass = klass



class Teacher(People):
    def __init__(self, name, subject):
        People.__init__(self, name)
        self.subject = subject




teachers = [Teacher('Teacher 1', 'Subject 1'),
            Teacher('Teacher 2', 'Subject 2'),
            Teacher('Teacher 3', 'Subject 3'),
            Teacher('Teacher 4', 'Subject 4'),
            Teacher('Teacher 5', 'Subject 3'),
            Teacher('Teacher 6', 'Subject 2')]



klasses = ["6A", "7A", "8A"]

students = []
for i in range(1,30):
    students.append(Student("Student %s"%i, "Mum %s"%i, "Dad %s"%i, klasses[random.randint(0,2) ]))


#1:
R = []
for i in students:
    if i.klass not in R:
        R.append(i.klass)
print(R)

#2:
R = []
k = input("Введите название класса")
for i in students:
    if k == i.klass:
        R.append(i.name)
print("В данном классе обучаются следующие студенты: %s" %R)

#3: К сожалению, у меня не получилось связать учителя, класс и учеников.
# Долго боролся -

#4:
R = []
k = input("Введите имя ученика")
for i in students:
    if k == i.name:
        R.append(i.mum)
        R.append(i.dad)
print("Родители данного ученика: %s" %R)











