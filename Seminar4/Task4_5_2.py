#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

#Пример двух заданных многочленов:
#23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

#Результат:
#40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import math

def get_polinom(string): 
     string1_1=string.replace('+',' ').replace('-',' -').replace('*',' ').replace('x','')
     string1_2=string1_1.split(' ')
     if (string1_2[0]==''):
      string1_2.remove('')

     size=len(string1_2)
#print(size1)
     a=[]
     p=[]
     for i in range(0,size):
        if i % 4 ==0:
          a.append(int(string1_2[i]))
        if i % 4 ==3:
          p.append(int(string1_2[i]))   

     a=a[::-1] # коэффициенты  многочлена
     p=p[::-1] # степени  многочлена


     for i in range(0,max(p)+1):
         if i  not in p:
           a.insert(i,0)

     return a

with open('file_polinom1.txt', 'r') as f:
    string=f.readline()
    print(string)
a1=get_polinom(string)

with open('file_polinom2.txt', 'r') as f:
    string=f.readline()
    print(string)
a2=get_polinom(string)
    
l1=len(a1)
l2=len(a2)
if l1>l2:
    for i in range(l2+1,l1+1):
          a2.append(0)
else:
      for i in range(l1+1,l2+1):
          a1.append(0)        

sum=[]
s=max(l1,l2)# выбираем наибольшую степень-степень результата

for i in range(0,s):
    sum.append(a1[i]+a2[i])
#print(sum)  коэффициеты суммы
sum=sum[::-1]



polinom=''
i=0
while s>0:
        
         polinom=polinom+(f'{sum[i]}*x**{s-1}+')
         s=s-1
         i=i+1

polinom1=polinom[:-1]  
polinom2=polinom1.split('+')


for i in range(0, len(polinom2)): 
    if polinom2[i][0]=='0':
            polinom2[i]=''
    
         
  
polinom_result=''
for i in range(0, len(polinom2)):
  polinom_result=polinom_result+(f'{polinom2[i]}+')
  polinom_result1=polinom_result.replace('++','+').replace('+-','-')

polinom_result2=polinom_result1[:-1] 

   
    
         
    



with open('file_result1.txt', 'w') as f:
    f.write(polinom_result2)
