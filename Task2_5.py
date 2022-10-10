#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной 
# строке одно число.


def get_list(n):
  import random
  list=[]
  for i in range(0,n):
    list.append(random.randint(-n,n))
  return list

n=int(input('Введите число: '))
list=get_list(n)
print( list)


f = open("file.txt", "r")

lines = f.readlines()
list1=[]

for line in lines:
  list1.append(int(line.strip()))
print('Последовательность позиций',list1)
f.close

n1=int(input('ВВедите номер позиции первого элемента '))
n2=int(input('ВВедите номер позиции второго элемента '))
if (n1>n)or(n2>n):
  print('решения нет')
else:  
       result=list[n1-1]*list[n2-1]
       print('Произведение элементов, стоящих на позициях', n1, 'и', n2, 'равно', result)