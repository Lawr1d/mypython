import random
import math
import sys

def getPlayPole():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def displayBoard(board):
    strOne = '    '
    for i in range(1,6):
        strOne += ' '*9 + str(i)

    print(strOne)
    print('   '+('0123456789'*6))
    print()

    for stroka in range(15):
        if stroka<10:
            strPol = ' '
        else:
            strPol = ''

        strBoard = ''
        for stalbec in range(60):
            strBoard += board[stalbec][stroka]

        print('%s%s %s %s' % (strPol, stroka, strBoard, stroka))


    print()
    print('   '+('0123456789'*6))
    print(strOne)

def getRandomChests(kolChests):
    chasts = []
    while len(chasts)<kolChests:
        newChasts = [random.randint(0,59),random.randint(0,14)]
        if newChasts not in chasts:
            chasts.append(newChasts)
    return chasts


        
def isOnBoard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def vopros(textVoprosa):
    print(textVoprosa)
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'ye') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
            
        elif (otvet == 'нет') or (otvet == 'не') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False

def makeMove(board,chasts,x,y):
    minDisrance = 100
    for cx,cy in chasts:
        distanciya = math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if distanciya < minDisrance:
            minDisrance = distanciya
    minDisrance = round(minDisrance)

    if minDisrance == 0:
        chasts.remove([x,y])
        print('Вы нашли сундук с сокровищами на затонувшем корабле')
        return True

    else:
        if minDisrance < 10:
            board[x][y] = str(minDisrance)
            print('Сундук с сокровищами обнаружен на расcтоянии %s единиц от гидролокатора.' % (minDisrance))
            return False
        else:
            board[x][y] = 'X'
            print('Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости')
def enterPlayerMove(predHoda):
    print('''Где следует опустить гидролокатор?
    (координаты: 0-59 0-14)
    (или набирите "Выход" для прекращения игры''')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру!')
            sys.exit()

        move = move.split()

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in predHoda:
                print('Вы уже опускали сюда гидролокатор')
            else:
                return [int(move[0]),int(move[1])]
        else:
            print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')


def showInstructage():
    print('''Инструктаж:
        Вы - Капитан корабля, плывущего за сокровищами. Ваша задача - с помощью  гидролокатора найти три
    сундука с сокровищами в затонувших судах на дне океана, но  гидролокаторы очнь просто  и  определяют
    только расстояние, но не направление.
        Введите координаты, чтобы опустить гидролокатор в воду, на карте будет показано число, обозначаю-
    щее на каком расстоянии находиться ближайший сундук, или будет показана буква X,  обозначающая,  что
    сундук в области действия гидролокатора не обнаружен. На примере карты ниже  метки  C - это  сундуки.
    цифра 3 обозначает, что ближайший сундук находиться на отдалении в 3 единицы.

                1         2         3
      012345678901234567890123456789012

    0 `---`-`--```-----```-`---`-``-`-- 0
    1 -`-```-`-`---`--`````----`-`--``- 1
    2 ``-`C--3-````C--`-``-`--`-`--`--` 2
    3 -```-`-----```-`-``-`-`--`-`--``- 3
    4 --`-``-``-``C-`-`--`--`-`-`-`--`` 4
    
      012345678901234567890123456789012
                1         2         3

    (во время игры сундуки на карте не обозначаються)
    Нажмите клавишу Enter, чтобы продожить...
    ''')
    input()
    print('''         Если гидролокатор опущен прямо на сундук, вы можете го поднять, друге гидролкаторы
    обновят данные расположении ближайшего сундука. Сундуки ниже находятся вне диапазона локатора, поэтому
    отображаеться буква X.
    
                1         2         3
      012345678901234567890123456789012

    0 `---`-`--```-----```-`---`-``-`-- 0
    1 -`-```-`-`---`--`````----`-`--``- 1
    2 ``-`X--7-```-`C-`-``-`--`-`--`--` 2
    3 -```-`-----```-`-``-`-`--`-`--``- 3
    4 --`-``-``-``C-`-`--`--`-`-`-`--`` 4
    
      012345678901234567890123456789012
                1         2         3
    
    Нажмите кнопку Enter чтобы продолжить...
    ''')
    input()
    print('''
        Сундуки с сокровищами во время игры не перемещаются. Гидролокаторы определяют сундуки на расстоянии
    до 9 единиц. Попробуйте поднять все 3 сундука до того, как все гидролокаторы будут опущены в воду.

    УДАЧИ!

    Нажмите Enter, чтобы продолжить...
    ''')
    input()

# ************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ************************************************
#spis = [[4,3],[13,8]]
#hod = enterPlayerMove(spis)
#print(hod)

print('Охотник за сокровищами.')
print()
if vopros('Хотите прочитать инструктаж?'):
    showInstructage()

while True:
    # делаем настройки игры
    # сколько гидролокаторов мы даем игроку
    kolGidro = 20
    # создадим игровое поле
    theBoard = getPlayPole()
    # размещаем три сундука на нашем игровом поле
    sunduki = getRandomChests(3)
    # покажем игровое поле игроку
    displayBoard(theBoard)
    # создадим пустую переменную, куда будем помещать все ходы игрока
    # это будет пустой список
    hodyGamer = []

    while kolGidro > 0:
        # сообщим игроку сколько у 
        # него осталось свободных гидролокаторов
        # и сколько сундуков с сокровищами осталось найти
        if len(sunduki)==1:
            okon = ''
        else:
            okon = 'a'
        print('Осталось %s неиспользованных гидролокаторов. Необходимо найти еще %s сундук%s' % (kolGidro, len(sunduki),okon))
        # примем от игрока координаты куда он хочет опустить гидролокатор
        x,y = enterPlayerMove(hodyGamer)
        # добавим принятые от игрока координаты в списокуже сделанных игроком ходов
        hodyGamer.append([x,y])


        if makeMove(theBoard,sunduki,x,y):
            # обновить все гидролокаторы
            a = 'вместо этого будет цикл'
        # показать игровое поле
        displayBoard(theBoard)
        # уменьшаем кол-во сундуков на 1

        print()
        input()



#while True:
#    a = int(input('Введите первую координату:     '))
#    b = int(input('Введите вторую координату:     '))
#    print(isOnBoard(a,b))
#    if vopros():
#        break