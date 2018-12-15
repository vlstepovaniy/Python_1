__author__ = 'Степованый Владислав Геннадьевич'
"""EASY"""

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
list = []
list = [random.randint(-10, 10) for i in range(10)]
new_list = []
for j in list:
    new_list.append(j**2)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random   #Генератор фруктов
fruits = {1: "яблоко", 2:"ананас", 3:"персик", 4:"груша", 5:"апельсин"}
list_1 = [random.randint(1, 5) for i_1 in range(5)]
fruit_list_1 = []
for i_1 in list_1:
    fruit_list_1.append(fruits[i_1])
print(fruit_list_1)

list_2 = [random.randint(1, 5) for i_2 in range(5)]
fruit_list_2 = []
for i_2 in list_2:
    fruit_list_2.append(fruits[i_2])
print(fruit_list_2)

Final_list = []
for j in fruit_list_1:
    for k in fruit_list_2:
        if j == k and Final_list.count(k) < 1:
            Final_list.append(k)

print(Final_list)




# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
list = []
list = [random.randint(-10, 10) for i in range(100)]
new_list = []
for i in list:
    if i % 3 == 0 or i > 0 or i % 4 != 0:
        new_list.append(i)
print(new_list)

"""NORMAL"""

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

#Вариант 1
import re
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

line_1 = re.compile(r'[^A-Z]+')
line_1 = line_1.findall(line)
print(line_1)

#Вариант 2

finish = []
jjj = ''
for symb in range(len(line)):
    if line[symb].islower():
        jjj += line[symb]
    else:
        if line[symb - 1].islower():
            finish.append(jjj)
            jjj = ''
print(finish)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

#Вариант 1
import re
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

line_3 = re.compile(r'([a-z]{2})([A-Z]+)([A-Z]{2})')
group = line_3.findall(line_2)
final_list = [x[1] for x in group]
print(final_list)

#Вариант 2
final_2 = []
jjjj = ''
for symb_2 in range(len(line_2)):
    try:
        if (line_2[symb_2 - 2].islower() and line_2[symb_2 - 1].islower() and line_2[symb_2].isupper()) or len(
                jjjj) > 0:
            jjjj += line_2[symb_2]
            if line_2[symb_2 + 1].isupper() and line_2[symb_2 + 2].isupper():
                if line_2[symb_2 + 2].isupper() and line_2[symb_2 + 3].isupper():
                    pass
                else:
                    final_2.append(jjjj)
                    jjjj = ''

            else:
                jjjj = ''

    except IndexError:
        pass

print(final_2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import re

with open('fileles4.txt', 'w') as f:
    n = [str(random.randint(0, 9)) for _ in range(2499)]
    n = str(random.randint(1, 9)) + ''.join(n)
    f.write(n)

with open('fileles4.txt', 'r') as f:
    file_number = f.readline()
    pattern = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
              '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
    seq = re.findall(pattern, file_number)
    print(seq)
    longest_seq = []
    [longest_seq.insert(0, x) for x in seq if len(x) > len(longest_seq)]
print(longest_seq[0])