#Подключаем модуль      2324
import random

attNumber = 0

print("Привет! Как тебя зовут?")
myName = input()

number = random.randint(1,100)
print("Что ж, "+myName+", я загадывая число от 1 до 100")

for attNumber in range(10):
 #   print("Попробуй угадать") # четыре
    quess = input("Попробуй угадать ")
    quess = int(quess)

    if quess < number:
        print("Твоё число слишком маленькое ") # восемь пробелов
    
    if quess > number:
        print("Твоё число слишком большое ") # восемь пробелов

    if quess == number:
        break

if quess == number:
    attNumber = str(attNumber + 1)
    print("Отлично, "+myName+"! ты справился с задание за "+attNumber+" попытки!")

if quess != number:
    number = str(number)
    print("Увы, я загадал число "+number+".")