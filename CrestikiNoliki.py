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