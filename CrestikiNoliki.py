from operator import truediv
import random
def DisplayBoard(board):
    print('''
    ''')
    print('     '+board[7]+'|'+board[8]+'|'+board[9])
    print('     '+'-+-+-')
    print('     '+board[4]+'|'+board[5]+'|'+board[6])
    print('     '+'-+-+-')
    print('     '+board[1]+'|'+board[2]+'|'+board[3])
    print('''
    ''')

def Proverka():
    while True:
        print('Введите каким значком вы будете играть X или O на англ. раскладке')
        vibor = input().upper()
        if vibor == 'X' or 'O':
            break

    if vibor == 'X':
        return ['X','O']
    else:
        return ['O','X']

def WhoGoesPerv():
    random.randint()

print(DisplayBoard([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']))
print(Proverka())

def board(x):
    x = []
    for i in board:
        x.append(i)
    return x

def ProvVybora():
    while move not in '1 2 3 4 5 6 7 8 9'.split()or not iSF(board,int(move)):
        print('Ваш следующий ход? Введите номер ячейки. (1-9)')
        move = input()
    return int(move)

def ii(board,movesList):
    possibleMoves = []
    for i in movesList:
        if iSF(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
board = [' ']*10
mL = [1,3,7,9]

hod = ii(board,mL)
print(hod)

DisplayBoard(board)

board[1] = 'X'
board[7] = 'X'
board[9] = 'X'

hod = ii(board,mL)
print(hod)

DisplayBoard(board)