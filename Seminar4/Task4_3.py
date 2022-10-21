#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.
#Пример:
#47756688399943 -> [5]
#1113384455229 -> [8,9]
#1115566773322 -> []

from tokenize import Number
#from typing import Sequence


dictionary=\
{ 
    'dig0':0,
    'dig1':1,
    'dig2':2,
    'dig3':3,
    'dig4':4,
    'dig5':5,
    'dig6':6,
    'dig7':7,
    'dig8':8,
    'dig9':9
}
#print(dictionary)
print(dictionary.values())

Number=int(input('введите последовательность цифр: '))
#print(Number)
print(dictionary.keys)
NumberSequece = []
i = 0
while Number > 9:
    NumberSequece.append(Number% 10)
    i += 1
    Number //= 10
NumberSequece.append(Number)

reverceNumber=NumberSequece[::-1]
print(reverceNumber)
count=0
for i in range(0,len(reverceNumber)):
    if  reverceNumber[i] == dictionary.get('dig0'):
       count=count+1
    

if count>1:
 x=dictionary.get('dig0')
for i in range(0,len(reverceNumber)):   
    reverceNumber.remove(x)

print(reverceNumber)

