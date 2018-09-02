import numpy as np  # импортирую модуль numpy
import random

x=random.randint(0, 12)
y=random.randint(0, 12)

array=np.random.randint(-3,11, size=(y, x))   #создаю массив
print(array)   #вывод массива
list=[]
for i in range (y):                         #цикл по вертикали
    sum=0
    counter=0
    for z in range (x):                     #цикл по горизонтали
        if array[i,z] >= 0:
            sum= sum + array[i, z]
            counter = counter+1
        else:
            break
    if counter >= x:
        sum = 0
    list.append(sum)
print(list)
