def get_list(n):
  import random
  list=[]
  for i in range(0,n):
    list.append(random.randint(20,80))
  return list

def  mix_list(list):
  import random
  list=list[:]
  length_list=len(list)

  for i in range(length_list):
    index_element=random.randint(0,length_list-1)
    temp=list[i]
    list[i]=list[index_element]
    list[index_element]=temp
    
  return list


n=int(input('Введите количество элементов в списке'))
list=get_list(n)
print(list)

list=mix_list(list)

print()
print(list)
