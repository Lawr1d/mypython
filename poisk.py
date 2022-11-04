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

print(getPlayPole())