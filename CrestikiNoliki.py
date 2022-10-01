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

def hod(board,pr,move):
    board[move] = pr

def Proverka2(board,pr):
    return((board[1]==pr and board[2]==pr and board[3]==pr) or
    (board[4]==pr and board[5]==pr and board[6]==pr) or
    (board[7]==pr and board[8]==pr and board[9]==pr) or
    (board[7]==pr and board[4]==pr and board[1]==pr) or
    (board[8]==pr and board[5]==pr and board[2]==pr) or
    (board[9]==pr and board[6]==pr and board[3]==pr) or
    (board[9]==pr and board[5]==pr and board[1]==pr) or
    (board[7]==pr and board[5]==pr and board[3]==pr))

def WhoGoesPerv():
    if random.randint(0,1) == 0:
        return 'компьютер'
    else:
        return 'человек'


#print(DisplayBoard([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']))
#print(Proverka())

def board2(x):
    x = []
    for i in board:
        x.append(i)
    return x

def iSF(board, move):
    return board[move] == ' '

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

hod = ii(board,mL)
print(hod)

DisplayBoard(board)

def HodPC(board,computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    for i in range(1,10):
        BoardCopy = board2(board)
        if iSF(boardCopy,i):
            hod(boardCopy,computerLetter)
            if Proverka2(boardCopy,computerLetter):
                return i

    for i in range(1,10):
        boardCopy = board2(board)
        if iSF(board,i):
            hod(boardCopy,playerLetter,i)
            if Proverka2(boardCopy,playerLetter):
                return i

def isdf(board):
    for i in range(1,10):
        if iSF(board,i):
            return False
        return True

################
#ТЕЛО ПРОГРАММЫ#
################

print('Игра "КРЕСТИКИ-НОЛИКИ"')

while True:
    theBoard = [' ']*20

    playerLetter, computerLetter = Proverka()

    turn = WhoGoesPerv()
    print(''+turn+' ходит первым.')

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'человек':
            DisplayBoard(theBoard)
            move = ProvVybora(theBoard)
            hod(theBoard,playerLetter,move)


        if Proverka2(theBoard,playerLetter):
            DisplayBoard(theBoard)
            print('Поздравляем! Ты выиграл!')
            gameIsPlaying = False
        else:
            if isdf(theBoard):
                DisplayBoard(theBoard)
                print('Ничья!')
                break
            else:
                turn = 'Компьютер'
    else:
        move = HodPC (theBoard, computerLetter)
        hod(theBoard,computerLetter,move)

        if Proverka2(theBoard,computerLetter):
            DisplayBoard(theBoard)
            print('ИИ оказался сильнее! Вы проиграли')
            gameIsPlaying = False
        else:
            if isdf(theBoard):
                DisplayBoard(theBoard)
                print('Ничья!')
                break
            else:
                turn = 'Человек'
    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break