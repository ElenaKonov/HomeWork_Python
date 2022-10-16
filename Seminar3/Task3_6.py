#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных 
# чисел.

#Xn+1=(aXn+c)mod m

import time


def list_random(size):
    
   seed=time.time()
   r=[size]
   r[0]=round(seed%m)
   for i in range(1, size):
    r.append(round(((a*r[i-1]+c) % m)))
   return r

size=int(input('Введите размер списка случайных элементов: '))


if (size<=0):
     print('Данные введены неверно')
else:
     m=int(input('Введите значение модуля m:'))
     a=int(input('Введите коэффициент a:'))
     c=int(input('Введите значение коэффициента с:'))
         
     
r=list_random(size)       
print(r)
