#Реализуйте алгоритм перемешивания списка.

list=[]
n=int(input('Введите количество элементов в списке'))
for i in (0,n+1):
    list.append(2*i+3)
print(list)