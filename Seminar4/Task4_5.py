#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

#Пример двух заданных многочленов:
#23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

#Результат:
#40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

import math

with open('file_polinom1.txt', 'r') as f:
    string=f.readline()
    print(string)
    
string1_1=string.replace('+',' ').replace('-',' -').replace('*',' ').replace('x','')
string1_2=string1_1.split(' ')
if (string1_2[0]==''):
    string1_2.remove('')

size1=len(string1_2)
#print(size1)
a1=[]
p1=[]
for i in range(0,size1):
    if i % 4 ==0:
       a1.append(int(string1_2[i]))
    if i % 4 ==3:
          p1.append(int(string1_2[i]))   

a1=a1[::-1] # коэффициенты первого многочлена
p1=p1[::-1] # степени первого многочлена
#print(a1)
#print(p1)
#print(max(p1))

for i in range(0,max(p1)+1):
     if i  not in p1:
        a1.insert(i,0)
#print(a1)    Недостающие степени берем нулями    
  


with open('file_polinom2.txt', 'r') as f:
    string=f.readline()
    print(string)
    
string2_1=string.replace('+',' ').replace('-',' -').replace('*',' ').replace('x','')
string2_2=string2_1.split(' ')


size2=len(string2_2)
a2=[]
p2=[]
if (string2_2[0]==''):
    string2_2.remove('')

size2=len(string2_2)

for i in range(0,size2):
     if i % 4 ==0:
        a2.append(int(string2_2[i]))
     if i % 4 ==3:
        p2.append(int(string2_2[i]))   

a2=a2[::-1]

p2=p2[::-1]

for i in range(0,max(p2)+1):
     if i  not in p2:
        a2.insert(i,0)
#print(a2)        
  

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
#sum1=str(sum)
#for i in range(0,s):
    #if sum[i]>0:
        #sum[i]= +sum[i]
#print(sum)  


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


