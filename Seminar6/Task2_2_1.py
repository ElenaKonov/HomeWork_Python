#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#num=int(input("ВВедите число"))
#n=1
#for i in range(1, (num+1)):
    #n=n*i
    #print(n, end= ' ')
import math
num=int(input("ВВедите число: "))
list=[math.factorial(n) for n in range(1, (num+1))  ]
print(list)
