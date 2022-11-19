import random

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
        

            


theBoard = getPlayPole()
displayBoard(theBoard)