import os #В разделе Run->Edit configurations поставить галочку в пункте Emulate...
strZ="  0 1 2" # не изменяемая
str0="---" # 0-2 игровые строки
str1="---"
str2="---"
pole=[list(str0),list(str1),list(str2)]
step=[] #шаги, за шаг сохраняется кортеж из двух координат, нечетный кортеж - кретик, четный - нолик.
debug=False #если есть ошибка
def clear(): os.system('cls') # код, который стирает экран

def outputer(): #код, который выводит на экран
    global strZ,pole
    print ("Ход №", len(step)+1)
    print(strZ,'0 '+' '.join(pole[0]),'1 '+' '.join(pole[1]),'2 '+' '.join(pole[2]), sep="\n")

def inputer(): #код, который принимает значения, проверяет их валидность
    global step, debug
    if len(step)%2==0:
        queue = "крестик"
    else:
        queue = "нолик"
    xy = ""
    while True:
        try:
            xy = tuple(map(int, input(f"Игрок {queue}, введите координаты x,y через пробел").split()))
        except ValueError:
            print("Надо вводить целые числа, через пробел")
            debug=True
        else:
            if xy in step:
                print("Клетка занята!")
                debug = True
            elif len(xy) !=2:
                print("Пропущена координата!")
                debug = True
            elif any([xy[0]>2, xy[1]>2, xy[0]<0, xy[1]<0]):
                print("Значение за пределами координатной сетки!")
                debug = True
            else:
                step.append(xy)
                debug = False
        if debug==False:
            break


def gamer(): #код, который ставит крестик
    global step,pole
    x,y=step[-1][0],step[-1][1]
    if len(step)%2==0:
        pole[x][y] = "o"
    else:
        pole[x][y] = "x"

def winner(a): #универсальный код для о и х
    global pole
    win=0
    for i in range(3):
        if all([pole[i][0] == a, pole[i][1] == a, pole[i][2] == a]):
            win = 1
        if all([pole[0][i] == a, pole[1][i] == a, pole[2][i] == a]):
            win = 2
    if all([pole[0][0] == a, pole[1][1] == a, pole[2][2] == a]):
        win = 3
    if all([pole[0][2] == a, pole[1][1] == a, pole[2][0] == a]):
        win = 4
    return win

while True:
    outputer()
    inputer()
    gamer()
    if winner('x') > 0:
        clear()
        outputer()
        print("Крестик выиграл!")
        break
    clear()
    outputer()
    if len(step) > 8:
        clear()
        outputer()
        print("Ничья!")
        break
    inputer()
    gamer()
    if winner('o') > 0:
        clear()
        outputer()
        print("Нолик выиграл!")
        break
    clear()


