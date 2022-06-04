# Это игра напёрстки
import random,time

#print("Как тебя зовут?")
#myName = input

def displayIntro():
    print("""вы идёте по рынку и видите человека сидящего за
    столом. На столе перед ним находятся три наперстка. Он показывает маленький шарик,
    который накрывает одним из напёрстков...""")
    time.sleep(2)
    print("""После этого он начинает перемешивать все напёрстки с большой
    скоростью, что даже трудно отследить расположение напёрстка с шариком.""")
    time.sleep(2)
    print("""При этом он не перестаёт произносить фразу 'Кручу верчу запутать хочу.'""")
    
def playGames():
    naperstok = random.randint(1,3)
    print("""Вы решили испытать удачу, угадать под каким из напёрстков находится
    шарик! Укажите номер напёрсткаб введя одно из чилел '1', '2', '3'.""")
    vybor = input()
    if naperstok == int(vybor):
        print("Вы победили")

    if naperstok != int(vybor):
        print("Вы проиграли")

#print("Как тебя зовут?")
#myName = input()
#print("ПРЕДЫСТОРИЯ")
#uslovie = input()
#while uslovie:
displayIntro()
displayIntro()
displayIntro()
displayIntro()
#    playGames()