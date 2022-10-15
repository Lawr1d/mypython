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

def display(kubiki,kubik1,kubik2,OchG,OchK,gamer):
    print(gamer)
    print(kubiki[kubik1])
    print(kubiki[kubik2])
    print()
    print('Количества очков:')
    print('Вы - '+str.OchG+' Компьютер - '+str.OchK+'')

def Hod():
    print('Нажмите (Б) чтобы бросить')
    while True:
        otvet = input().upper().startswith('Б')
        if (otvet == 'Б') or (otvet == 'б'):
            return True
        else:
            print('Я вас не понял нажмите (Б) чтобы бросить кубик')

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
OchkiKup()
display(kubiki,kubik1,kubik2,OchG,OchK,gamer)
Hod()
Hod2()