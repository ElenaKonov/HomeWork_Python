#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10







def get_bynarycod(n):
  
  m=''
  while n>0:
     m=str(n%2)+m
     n=n // 2
  return m


n=int(input('Введите число: '))
bynary_codN=get_bynarycod(n)

print( 'Двоичный код числа ', n, ' = ', bynary_codN)



