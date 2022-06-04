def playAgen():
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

if playAgen():
    print('Игра продолжается')
else:
    print('Игра заканчивается')