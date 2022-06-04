import random
def sV():
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
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
    ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
    ===''','''
  +---+
 [O]  |
 /|\] |
 / \  |
    ===''','''
  +---+
 [O]  |
[/|\] |
 / \  |
    ===''']
    return HANGMAN_PICS

words={'животные':'аист акула осьминог белка буйвол воробей бобр бабочка антилопа барсук медведь кабан крокодил верблюд корова лягушка жираф свинья крыса бурундук хорек осел буйвол утка конь козер калибри крот лангуст ласточка рысь тигр слон козел обезьяна баран кролик зебра орел гусь носорог бегемот'.split(),
'фигуры':'квадрат круг треугольник пятиугольник параллелепипед конус цилиндр пирамида ромб прямоугольник параллелограм сфера'.split(),
'цвета':'красный оранджевый желтый зеленый голубой синий фиолетовый коричневый белый черный серый бирюзовый розовый бежевый пурпурный золотой серебряный малиновый салатовый болотный бронзовый бордовый ванильный грушевый индиго кварцевый кирпичный коралловый кофейный кремовый лаймовый лазурный небесный нефритовый персиковый песочный сапфировый'.split()}
def vybSlova(wordsList):
    wordKey = random.choice(list(wordsList.keys()))

    wordsIndex = random.randint(0, len(wordsList[wordKey])-1)
    return [wordsList[wordKey][wordsIndex],wordKey]

def funk(errorB,yesB,sicretS,hm):
    print(hm[len(errorB)])
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
            print('Вы уже писали эту букву')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    print('Вы хотите сыграть ещё раз? (Да или нет)')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'ye') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return slozhnost()
            
        elif (otvet == 'нет') or (otvet == 'не') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False

        else:
            print('''я вас не понял!
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')

def slozhnost():
    print('''Выберите сложность игры:
    Введите "Л" для легкого режима
    Введите "С" для среднего режима
    Введите "Т" для тяжелого режима''')
    while True:
        otvet = input().upper()
        if len(otvet) != 1:
            print('Введите только одну букву')
        elif otvet not in 'ЛСТ':
            print('Введите "Л", "С" или "Т"')
        else:
            return otvet


def delVis(uS,vis):
    if uS == 'С':
        del vis[10]
        del vis[9]
    elif uS == 'Т':
        del vis[10]
        del vis[9]
        del vis[8]
        del vis[7]


delV = True
errorB = ''
yesB = ''
gameOver = False
sicretS,keyW = vybSlova(words)

while True:
    if delV:
        hm = sV()

        BS = slozhnost()
        delVis(BS,hm)
        delV = False

    if BS == 'Л':
        print(keyW)
    funk(errorB,yesB,sicretS,hm)

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
        if len(errorB) == len(hm) - 1:
            funk(errorB,yesB,sicretS,hm)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+' и угадано букв:'+str(len(yesB))+'. Было загадано слово "'+sicretS+'".')
            gameOver = True

    if gameOver:
        if playAgain():
            errorB = ''
            yesB = ''
            gameOver = False
            sicretS,keyW = vybSlova(words)
            delV = True
        else:
            break