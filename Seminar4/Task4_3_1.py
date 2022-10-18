#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.
#Пример:
#47756688399943 -> [5]
#1113384455229 -> [8,9]
#1115566773322 -> []
Number=int(input('введите последовательность цифр: '))

NumberSequece = []
i = 0
while Number > 9:
    NumberSequece.append(Number% 10)
    i += 1
    Number //= 10
NumberSequece.append(Number)

reverceNumber=NumberSequece[::-1]
print(reverceNumber)


for j in range(0,10):
    c=reverceNumber.count(j)
    if c>1:
        for i in range(1,c+1):
         reverceNumber.remove(j)
print(reverceNumber)
        


   