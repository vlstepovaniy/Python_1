__author__ = 'Степованый Владислав Геннадьевич'

# Задача-1:
# # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# # из которой запущен данный скрипт.
# # И второй скрипт, удаляющий эти папки.
import os
import shutil
import sys

def create_delete_dir():
    path = []
    for i in range(1, 10):
        path.append("dir_%i" % i)
    print(path)

    choose = int(input("Введите 1 если необходимо создать директории  \nВведите 2 если необходимо удалить директории"))

    if choose == 1:
        for i_p in path:
            try:
                os.mkdir(i_p)
            except OSError:
                print ("Создать директорию %s не удалось" % i_p)
            else:
                print ("Успешно создана директория %s " % i_p)
    elif choose == 2:
        for i_p in path:
            try:
                os.rmdir(i_p)
            except OSError:
                print ("Удалить директорию %s не удалось" % i_p)
            else:
                print ("Успешно удалена директория %s" % i_p)
    else:
        print("Это ни 1 ни 2, введите корректное значение")


#
# # Задача-2:
# # Напишите скрипт, отображающий папки текущей директории.

def current_list_dir():
    direct = os.listdir()
    print(direct)
# к сожалению, не знаю как реализовать фильтр для папок
#
# # Задача-3:
# # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.



def copy_script(first_file, copy_file):
    first_file = sys.argv[0]
    copy_file = "backup.py"
    shutil.copy(first_file, copy_file)



"""Normal"""

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def current_dir(): #текущее положение
    global choose
    print("Сейчас открыта директория:%s" % os.getcwd())
    choose = int(input("1. Перейти в папку \n2. Просмотреть содержимое текущей папки\n3. Создать папку \n4. Удалить папку"))
    return choose

def create_dir():
    nn = input("Введите имя Вашей новой папки")
    try:
        os.mkdir(nn)
    except OSError:
        print ("Создать директорию %s не удалось" % nn)
    else:
        print ("Успешно создана директория %s " % nn)
    return

def delete_dir():
    dn = input("Введите имя папки, которую необходимо удалить")
    try:
        os.rmdir(dn)
    except OSError:
        print ("Удалить директорию %s не удалось" % dn)
    else:
        print ("Успешно удалена директория %s" % dn)
    return


current_dir()
if choose == 1:
    direct = os.listdir()
    print("Куда пойдем?")
    print(direct)
    new_path = input() #хотел реализовать словарь - как список папок, но не знаю как выполнить easy2
    os.chdir(new_path) # и как задать последовательный ключ для каждой папки
    current_dir()

elif choose == 2:
    current_list_dir()

elif choose == 3:
    create_dir()

elif choose == 4:
    delete_dir()
