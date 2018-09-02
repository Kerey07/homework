import numpy as np  # импортирую модуль numpy

array=np.random.randint(100, size=(5, 5))   #создаю массив
print (array)   #вывод массива

y=0
while y < 5 :
    max=0
    x=0
    position=0
    while x < 5:
        old=array[y, y]
        if array[y, x] > max:
            max=array[y, x]
            position=x
        x+=1
    array[y, position]=old
    array[y,y]=max
    y+=1
print(array)

