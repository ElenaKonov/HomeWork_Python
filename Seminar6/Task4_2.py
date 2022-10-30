#Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.




prime_numbers=[] # найдем список простых чисел
 
for i in range(2,1000): # число 1 не является простым
         for j in range(2,i):
           if i%j==0:
            break
 
         else: prime_numbers.append(i)



def listOfdivisors(num):
    l=[]
    for k in prime_numbers:

       if ( num % k==0):
        l.append(k)
    return l
    

num=int(input('Введите число, для которого необходимо найти простые множители: '))
l=listOfdivisors(num)
print('Число', num , 'имеет в своем разложении следующие простые числа:' , l)