__author__ = 'Степованый Владислав Геннадьевич'
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random

barrel_number = []
card_numbers = []
for i in range(1, 91):
    card_numbers.append(i)
for i in range(1, 91):
    barrel_number.append(i)
playerscard = []
compscard = []

class player_card_line():
    def __init__(self):
        self.value = []
        e_s = []   # свободные места в карде, на случай если в строку заполнится менее 5 чисел
        q_pn = 0   # счетчик положительных чисел
        for I in range(1, 10):
            l_n = random.randint(0, 1) #random number
            if l_n == 1 and q_pn < 5:
                pop = card_numbers.pop(random.randint(0, len(card_numbers) - 1))
                self.value.append(pop)
                q_pn += 1
            else:
                self.value.append("  ")
                e_s.append(I)
        while q_pn < 5:
            l_n = random.randint(0, len(e_s)) #random number
            pop = card_numbers.pop(random.randint(0, len(card_numbers)-1))
            self.value.insert(l_n, pop)
            q_pn += 1
        while len(self.value) != 9:
            self.value.pop(e_s[0])

    def fill_card(self, card):   #Заполнить карту
        self.card =card
        for d in self.value:
            if type(d) == int:
                self.card.append(d)

    def cross_card(self, cross_number):
        self.cross_number = cross_number
        if cross_number in self.value:
            self.value.insert(self.value.index(self.cross_number), "-")








    """def sort(self):      Почему то не работает блок сортировки:(
        
        list_numbers = []   
        for i in self.value:
            if type(i) == int:
                list_numbers.append(i)
        n = 1
        while n < len(list_numbers):
            for i in range(len(list_numbers) - n):
                if list_numbers[i] > list_numbers[i + 1]:
                    list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
            n += 1
        for i in self.value:
            if type(i) == int:
                index = self.value.index(i)
                self.value.insert(index, list_numbers.pop(0))
        return self.value"""




def GAME():
    pc1 = player_card_line()   #Создание строк
    pc1.fill_card(playerscard)
    pc2 = player_card_line()
    pc2.fill_card(playerscard)
    pc3 = player_card_line()
    pc3.fill_card(playerscard)
    kk1 = player_card_line()
    kk1.fill_card(compscard)
    kk2 = player_card_line()
    kk2.fill_card(compscard)
    kk3 = player_card_line()
    kk3.fill_card(compscard)
    print(playerscard)
    pointsp = 0
    pointsc = 0
    while pointsp < 15 or pointsc < 15:
        print("ВАША КАРТА    ОЧКИ - {}\n_____________________________________________"
              "\n{}\n{}\n{}\n_____________________________________________".
              format(pointsp, pc1.value, pc2.value, pc3.value))
        print("\nКАРТА КОМПЬЮТЕРА    ОЧКИ - {}\n_____________________________________________"
              "\n{}\n{}\n{}\n_____________________________________________".
              format(pointsc, kk1.value, kk2.value, kk3.value))
        Barrel = barrel_number.pop(random.randint(10, len(barrel_number) - 1)) # Ввиду нерешенного бага с выпадением первых цифр двухзначныхчисел, выпадают числа больше 10
        print("Выпал бочонок с номером {}".format(Barrel))
        input1 = input("Зачеркнуть цифру? (y/n)")
        if input1 == "y":
            if Barrel in playerscard:
                pc1.cross_card(Barrel)
                pc2.cross_card(Barrel)
                pc3.cross_card(Barrel)
                pointsp += 1
                continue
            else:
                break
        elif input1 == "n":
            if Barrel in playerscard:
                break
            else:
                continue
        else:
            print("Не понимаю Вас, давайте попробуем еще разок")
        if Barrel in compscard:
            kk1.cross_card(Barrel)
            kk2.cross_card(Barrel)
            kk3.cross_card(Barrel)
            pointsc += 1

    print("Игра закончена")



GAME()

game = input("{Хотите сыграть еще раз?  y/n")
if game == "y":
    GAME()
elif game == "n":
    print ("Еще увидимся!")
else:
    print ("Не понимаю Вас")
















