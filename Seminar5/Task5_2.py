#Создайте программу для игры с конфетами человек против человека.

#Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'


# ПРОСТОЙ ВАРИАНТ ИГРЫ

N=150

while N>28:
    n1=int(input("Ход первого игрока: "))
    if n1>28 or n1<1:
        print("Ввели неккоректное число")
        continue
    
    
    n2=int(input("Ход второго игрока: "))
    if n2>28 or n2<1:
        print("Ввели неккоректное число")
        continue
    else: 
        N=(N-(n1+n2))

if (N==0):
    print("Выиграл второй игрок")
if (N!=0):
    print("Выиграл первый игрок")

     
