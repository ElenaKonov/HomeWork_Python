#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def get_list(n):
  import random
  list=[]
  for i in range(0,n):
    list.append(random.randint(-20,20))
  return list

def find_sum(list):
    sum=0
    for i in range(0,n):
        if (i%2==1):
         sum=sum+list[i]
    return sum        

n=int(input('Введите количество элементов в списке: '))
list=get_list(n)
print(list)
sum=find_sum(list)
print(sum)
