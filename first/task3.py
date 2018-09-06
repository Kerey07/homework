import numpy as np  # импортирую модуль numpy


answer_list = []

K_y = int(input('Введите K <=5 :'))
L_x = int(input('Введите L <=5 :'))

K_y = K_y - 1
L_x = L_x - 1

array = np.random.randint(2, size=(5, 5))  # создаю массив

for i in range(5):
    for ii in range(5):
        print(array[i, ii], end='  ')
        if ii == 4:
            print('\n')


for counter in range(4):
    x = 0
    y = 0
    quarter_sum = 0
    if counter == 1:
        for y in range(K_y):
            for x in range(L_x):
                quarter_sum = quarter_sum + array[y, x]
        answer_list.append(quarter_sum)
    elif counter == 0:
        for y in range(K_y):
            x = L_x + 1
            while x < 5:
                quarter_sum = quarter_sum + array[y, x]
                x += 1
        answer_list.append(quarter_sum)
    elif counter == 3:
        y = K_y + 1
        while y < 5:
            x = L_x + 1
            while x < 5:
                quarter_sum = quarter_sum + array[y, x]
                x += 1
            y += 1
        answer_list.append(quarter_sum)
    elif counter == 2:
        y = K_y + 1
        while y < 5:
            for x in range(L_x):
                quarter_sum = quarter_sum + array[y, x]
            y += 1
        answer_list.append(quarter_sum)
print(answer_list)