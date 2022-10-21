
Number=int(input('введите последовательность цифр: '))

NumberSequece = []
i = 0
while Number > 9:
    NumberSequece.append(Number% 10)
    i += 1
    Number //= 10
NumberSequece.append(Number)

reverceNumber=NumberSequece[::-1]
#print(reverceNumber)
c=reverceNumber.count(0)
if c>1:
   for i in range(1,c+1):

    reverceNumber.remove(0)

c=reverceNumber.count(1)

if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(1)

c=reverceNumber.count(2)

if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(2)


c=reverceNumber.count(3)

if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(3)

c=reverceNumber.count(4)

if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(4)

c=reverceNumber.count(5)
if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(5)  


c=reverceNumber.count(6)
if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(6) 

c=reverceNumber.count(7)
if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(7)

c=reverceNumber.count(8)
if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(8)

c=reverceNumber.count(9)
if c>1: 
   for i in range(1,c+1): 
    reverceNumber.remove(9)


print(reverceNumber)






#my_list = list(set(reverceNumber))


#print ("Список после удаления дубликатов: " + str(my_list))
