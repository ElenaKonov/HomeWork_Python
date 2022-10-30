#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


import random

List1=[x for x in range(-10,10)]
random.shuffle(List1)
print(List1)

if(len(List1)%2==0):
    size=len(List1)//2
else:
       size=len(List1)//2+1

List2=[List1[i]*List1[(len(List1)-1)-i]for i in range(0, size)]
print('Список произведений элементов:', List2)


