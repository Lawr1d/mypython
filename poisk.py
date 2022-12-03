import random
import math

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
#    for cx,cy in chasts:
# ************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ************************************************

while True:
    a = int(input('Введите первую координату:     '))
    b = int(input('Введите вторую координату:     '))
    print(isOnBoard(a,b))
    if vopros('Не хотите закончить проверку?'):
        break