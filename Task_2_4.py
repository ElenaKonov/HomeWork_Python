#Реализуйте алгоритм перемешивания списка.
import random


def get_list(n):
 list=[]
 for i in range(0,n+1):
    list.append(2*i+3)
 return list


n=int(input('Введите количество элементов в списке'))
list=get_list(n)
print(list)

list1=list[:]
random.shuffle(list1)
print(list1)