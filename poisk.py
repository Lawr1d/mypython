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
    while len(chasts)<=kolChests:
        newChasts = [random.randint(0,59),random.randint(0,14)]
        if newChasts not in chasts:
            chasts.append(newChasts)
    return chasts


        
def isOnBoard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def vopros():
    print('Не хотите закончить проверку?')
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
        chasts.remove(x,y)
        return 'Вы нашли сундук с сокровищами на затонувшем корабле'
    else:
        if minDisrance < 10:
            board[x][y] = str(minDisrance)
            return 'Сундук с сокровищами обнаружен на расcтоянии %s единиц от гидролокатора.' % (minDisrance)
        else:
            board[x][y] = 'X'
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости'
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
# ************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ************************************************
spis = [[4,3],[13,8]]
hod = enterPlayerMove(spis)
print(hod)








#while True:
#    a = int(input('Введите первую координату:     '))
#    b = int(input('Введите вторую координату:     '))
#    print(isOnBoard(a,b))
#    if vopros():
#        break