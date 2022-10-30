

##num=int(input("ВВедите число"))
#n=1
#for i in range(1, (num+1)):
    #n=n*i
    #print(n, end= ' ')


num=int(input("ВВедите число: "))
def fact(n): 
    if(n==1 or n==0):
         return 1 
    else: 
        return n*fact(n-1) 
list=[fact(n) for n in range(1, (num+1))  ]
print(list)
       
