#Реализуйте алгоритм перемешивания списка.



def get_list(n):
 list=[]
 for i in range(0,n):
    list.append(2*i+3) # список заполнен элементами последовательности 2n+3.
 return list


n=int(input('Введите количество элементов в списке'))
list=get_list(n)
print(list)

import random
list1=list[:]
random.shuffle(list1) # функция библиотеки
print(list1)