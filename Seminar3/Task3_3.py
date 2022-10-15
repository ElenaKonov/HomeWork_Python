#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

#*Пример:*

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def get_list(n):
  import random
  list=[]
  for i in range(0,n):
   list.append(random.randint(-10,10)+round(random.random(),2))

  return list

def get_fraction(list):
  list=list[:]
  list1=[]
  for i in range(0,len(list)):
    list1.append(round(((list[i])-int(list[i])),2))

  return list1




n=int(input('Введите количество элементов в списке: '))
list=get_list(n)
print('Иходный список:', list)

list1=get_fraction(list)
print(list1)

max_list1=list1[0]
min_list1=list1[0]

for i in range(0,len(list1)):
    if (list1[i]!=0 and list1[i]>max_list1):
            max_list1=list1[i]
    if(list1[i]!=0 and list1[i]<min_list1):
            min_list1=list1[i]

difference=max_list1-min_list1  
print(round(difference,2))


  