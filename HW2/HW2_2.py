#игра с конфетами
# 2 игрока

from random import randint


candys = 2021
Name1 = input("Игрок №1, введите свое имя: ")
Name2 = input("Игрок №2, введите свое имя: ")
print('Идет жеребьевка:')
Name1_game = randint(1, 2)
if Name1_game == 1:
    gamer1 = Name1
    gamer2 = Name2
    print('Начинает игру - ', Name1)
else:
    gamer1 = Name2
    gamer2 = Name1
    print('Начинает игру - ', Name2)
print('Игра началась! На столе ', candys, 'конфет')
while candys > 0:
    if candys > 28:
        a1 = int(input(f"Ходит {gamer1}. Сколько вы берете конфет: "))
        if a1 > 28:
            a1 = int(input("Вы не можете взять больше 28 конфет. Сколько вы берете конфет? "))
            candys -= a1
            print('На столе осталось', candys, 'конфет')
        else:            
            candys -= a1
            print('На столе осталось', candys, 'конфет')
    else:
        print(f"{gamer1} победил!")
        break   
    if candys > 28:
        a2 = int(input(f"Ходит {gamer2}. Сколько вы берете конфет: "))
        if a2 > 28:
            a2 = int(input("Вы не можете взять больше 28 конфет. Сколько вы берете конфет? "))            
            candys -= a2
            print('На столе осталось', candys, 'конфет')
        else:            
            candys -= a2
            print('На столе осталось', candys, 'конфет')
    else:
        print(f"{gamer2} победил!")
        break