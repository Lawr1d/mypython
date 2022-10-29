from ast import While
import random
def DisplayBoard():
    kubiki = ['''
    +-----+
   |       |
   |       |
   |       |
    +-----+''','''
    +-----+
   |       |
   |   *   |
   |       |
    +-----+''','''
    +-----+
   |     * |
   |       |
   | *     |
    +-----+''','''
    +-----+
   |     * |
   |   *   |
   | *     |
    +-----+''','''
    +-----+
   | *   * |
   |       |
   | *   * |
    +-----+''','''
    +-----+
   | *   * |
   |   *   |
   | *   * |
    +-----+''','''
    +-----+
   | *   * |
   | *   * |
   | *   * |
    +-----+''']
    return kubiki

def pravila():
    print('''Игра 21 очко.
    Хотите прочитать правила? (да или нет)''')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'ye') or (otvet == 'y'):
            return pravila2()
    
        elif (otvet == 'нет') or (otvet == 'не') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        
        else:
            print('''Я вас не понял!
Введите ответ еще раз (да или нет).''')

def pravila2():
    print('''    Вы бросаете кубики сколько угодно раз, пока не наберете число близкое к 21.
    Можно на любом броске передать ход компьютеру.
    Компьютер кидает также 2 кубика, пытаясь набрать количество очков больше чем у вас.
    Как только количество очков превысит количество ваших очков он перестает бросать кубики и говорит, что он выиграл.
    Если вы или компьютер набирают очков больше 21, то вы проигрываете''')

def nachalo():
    a = input('''
    Нажмите Enter чтобы начать игру''')

def OchkiKup():
    kubik1 = random.randint(1,6)
    kubik2 = random.randint(1,6)
    k = []
    k.append(kubik1)
    k.append(kubik2)
    return k

def display(kubiki,kubik1,kubik2,summaG,summaK,gamer):
    print(gamer)
    print(kubiki[kubik1])
    print(kubiki[kubik2])
    print()
    print('Количества очков:')
    print('Вы - '+str(summaG)+', Компьютер - '+str(summaK)+'.')
    print()

def playAgain():
    print('Вы хотите сыграть еще раз?')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'ye') or (otvet == 'y'):
            return True           
    
        elif (otvet == 'нет') or (otvet == 'не') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        
        else:
            print('''Я вас не понял!
Введите ответ еще раз (да или нет).''')

def Hod2():
    print('Нажмите (Б) чтобы бросить')
    while True:
        otvet = input().upper().startswith('П')
        if (otvet == 'П') or (otvet == 'п'):
            return True
        else:
            print('Я вас не понял нажмите (П) чтобы передать ход компьютеру')




#******************************************************************************************
#  ТЕЛО ПРОГРАММЫ  
#******************************************************************************************
pravila()

nachalo()

KtoBrosaet = 'Человек'
kubiki = DisplayBoard()
summaK = 0
summaG = 0
game = True
gamer = True
computer = True

while game:
    while gamer:
        kubik1,kubik2 = OchkiKup()
        summaG = summaG + kubik1 + kubik2
        display(kubiki,kubik1,kubik2,summaG,summaK,KtoBrosaet)       
        if summaG > 21:
            print('Вы проиграли')
            game = False
            gamer = False
        if game and not (input('(Б)росаем еще или (П)ередаем ход').upper() == 'Б'):
            gamer = False

while computer:
    while gamer:
        kubik1,kubik2 = OchkiKup()
        summaK = summaK + kubik1 + kubik2
        display(kubiki,kubik1,kubik2,summaG,summaK,KtoBrosaet)       
        if summaK > 21:
            print('Вы проиграли')
            game = False
            computer = False
        elif summaK > summaG:
            if game and not (input('(Б)росаем еще или (П)ередаем ход').upper() == 'Б'):
               computer = False