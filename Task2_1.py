#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

num=float(input('ВВедите число: '))
if (num<0): num=(-1)*num
num1=int(num)
num2=int(round(num%1,10)*pow(10,10))



sum1=0
while num1 > 0:
    sum1=sum1+num1 % 10
    num1=num1//10


sum2=0
while num2 > 0:
    sum2=sum2+num2 % 10
    num2=num2//10

print('Сумма всех цифр, введенного числа, равна', sum1+sum2)

