#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


def posled(N):
 sum=0
 for i in range(1, N+1):
    
    print(round((1+1/i)**i,4), end= ' ,')


   
def summa(N):
 sum=0
 for i in range(1, N+1):
    sum=sum+round((1+1/i)**i,4)
 return sum   
   

N=int(input('Введите число: '))
posled (N)
s=summa(N)

print('Сумма ',N, 'элементов последовательности равна', s)      
 
