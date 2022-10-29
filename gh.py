from ast import While
from operator import truediv
import random

KOL_CIFR = 3
KOL_POP = 10

def generator_Chisla():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(KOL_CIFR):
        secretNum += str(numbers[i])
    return secretNum

def podskazka(chislo_gamer,chislo_komp):
    if chislo_gamer == chislo_komp:
        return 'Вы угадали!'

    podskazka = []
    for i in range(len(chislo_gamer)):
        if chislo_gamer[i] == chislo_komp[i]:
            podskazka.append('Горячо')
        elif chislo_gamer[i] in chislo_komp:
            podskazka.append('Тепло')

    if len(podskazka) == 0:
        return 'Холодно'

    podskazka.sort()
    return ' '.join(podskazka)

def proverka_vvoda(num):
    print(num)
    if num == '':
        return False

    for i in num:
        print(i)
        if num not in '0 1 2 3 4 5 6 7 8 9'.split():
            print('Вышли с False')
            return False

    return True

def playAgain():
    print('Вы хотите сыграть ещё раз? (Да или нет)')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'ye') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'не') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''я вас не понял!
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')



#*******************************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
#*******************************************************************
print('Я загадаю %s-х значное число, которое вы должны отгадать' % (KOL_CIFR))
print('Я дам несколько подсказок...')
print('Если я говорю:          Это значит:')
print('   Горячо               Отгадана цифра и ее позиция.')
print('   Тепло                Отгадана цифра но не ее позиция.')
print('   Холодно              Не отгадана ни одна цифра.')

while True:
    secterNum = generator_Chisla()
    
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % (KOL_POP))
    
    popytka = 1
    while popytka <= KOL_POP:
        chislo_gamer = ''
        while len(chislo_gamer) != KOL_CIFR or not proverka_vvoda(chislo_gamer):
            print(len(chislo_gamer) != KOL_CIFR)
            print(not )
    if not playAgain():
        break