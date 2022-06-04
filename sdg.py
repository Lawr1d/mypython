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

slozhnost()