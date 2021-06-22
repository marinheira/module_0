import numpy as np
number=[i for i in np.random.randint(1,101,size=(10000))]
attempt=[] # Сюда будут записываться количество попыток за итерацию

for num in range(len(number)):
    count=1 # включаем первую попытку за итерацию
    success = False # ведь мы пока ещё не отгадали :)
    range_min = 0  # минимальный порог перебора вариантов
    predict = 0 # вариантов ответа пока нет
    if len(str(number[num]))!=2: # если число не двузначное, проверяем варианты 100 и 1...9
        if number[num]==100:
            predict = 100
            attempt.append(count)
            continue
        else:
            count+=1 # была попытка угадать 100 ли это, не получилось, +1 попытка
            for i in range(1,10):
                if i==number[num]:
                    predict=i
                    attempt.append(count)
                    break
                count+=1
    if predict==number[num]:
        continue

# если число симметричное - пытаемся перебрать все десять симметричных чисел
    if str(number[num])[0]==str(number[num])[1]:
        for i in range(1,10):
            if int(str(i)*2)==number[num]:
                predict=int(str(i)*2)
                attempt.append(count)
                break
            count+=1
    if predict == number[num]:
        continue

    if number[num]%2!=0: # сдвиг считывания (чет-нечет)
        range_min = 1
    else:
        range_min = 0
    if number[num]>53: # ставим место, откуда начинать проверять
        if number[num]>75:
            range_min += 76
        else:
            range_min += 54
    else:
        if number[num]>31:
            range_min += 32
        else:
            range_min += 10

# благодаря отсечению числа 98 удалось разбить ряд на 4 равных промежутка
# по результатам оценки Манна-Уитни (на этапе разработки), разницы между тем,
# перебирать ли по увеличению или уменьшению, не выявлено
    for i in range(range_min,range_min+21,2):
        if str(number[num])[0] == str(number[num])[1]: continue # Исключаем из перебора симметричные числа
        if i == number[num]:
            predict = i
            attempt.append(count)
            break
        count += 1
    if predict == number[num]:
        continue

# в конце проверяем оставшееся число, на него приходися 1% вероятности,
# поэтому, будучи загаданными, оно не будет вильно влиять на среднне число попыток
    if number[num]==98:
        predict = 98
        attempt.append(count)
        num+=1
        continue

import numpy
import math
print("Среднее число попыток\n(округлено в большую сторону): ",
      math.ceil(int(numpy.mean(attempt)))
      )
