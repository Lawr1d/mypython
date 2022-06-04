from ast import Index
import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 O   |
     |
     |
    ===''','''
 +---+
 O   |
 |   |
     |
    ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
words=['аист','акула','осьминог','белка','буйвол','воробей','бобр','бабочка','антилопа','барсук','медведь','кабан','крокодил','верблюд','корова','лягушка','жираф','свинья','крыса','бурундук','хорек','осел','буйвол','утка','конь','козер','калибри','крот','лангуст','ласточка','рысь','тигр','слон','козел','обезьяна','баран','кролик','зебра','орел','гусь','носорог','бегемот']
def vybSlova(wordsList):
    wordsIndex = random.randint(0, len(wordsList)-1)
    return wordsList[wordsIndex]

def funk(errorB,yesB,sicretS):
    print(HANGMAN_PICS[len(errorB)])
    print()

    print('Ошибочные буквы:',end=' ')
    for buk in errorB:
        print(buk,end=' ')
    print()

    leter = '_'*len(sicretS)
    
    for i in range(len(sicretS)):
        if sicretS[i] in yesB:
            leter = leter[:i]+sicretS[i]+leter[i+1:]
    print(leter)

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Введите только одну букву')
        elif guess in alreadyGuessed:
            print('Пожалуйста введите букву')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
            print('Пожалуйста введите БУКВУ')
        else:
            return guess

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

errorB = ''
yesB = ''
gameOver = False
sicretS = vybSlova(words)

while True:
    funk(errorB,yesB,sicretS)

    bukva = getGuess(errorB+yesB)

    if bukva in sicretS:
        yesB = yesB + bukva


        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            print('ДА! Секретное слово - "'+sicretS+'"! Вы угадали!')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(HANGMAN_PICS) - 1:
            funk(errorB,yesB,sicretS)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+' и угадано букв:'+str(len(yesB))+'. Было загадано слово "'+sicretS+'".')
            gameOver = True

    if gameOver:
        if playAgain():
            errorB = ''
            yesB = ''
            gameOver = False
            sicretS = vybSlova(words)
        else:
            break