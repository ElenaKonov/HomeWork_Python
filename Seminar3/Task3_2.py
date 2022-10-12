#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


def get_list(n):
  import random
  list=[]
  for i in range(0,n):
    list.append(random.randint(-10,10))
  return list

def get_list1(list):
   list=list[:]
   list1=[]
   if(len(list)%2==0):
    size=len(list)//2
   else:
    size=len(list)//2+1

   for i in range(0, size):
    list1.append(list[i]*list[(len(list)-1)-i])

   return list1


n=int(input('Введите количество элементов в списке: '))
list=get_list(n)
print('Иходный список:', list)
list1=get_list1(list)
print('Список произведений элементов:', list1)


