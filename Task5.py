#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# значений предикат.


    

list_x=[0,1]
list_y=[0,1]
list_z=[0,1]
for i in range(0,2):
 for j in range(0,2):
  for k in range(0,2):
   left_result = not(list_x[i] or list_y[j] or list_z[k])
   
   right_result = not list_x[i] and not list_y[j] and not list_z[k]
   print(list_x[i], list_y[j], list_z[k], left_result, right_result)
 
print()     


            
    

for i in range(0,2):
 for j in range(0,2):
  for k in range(0,2):
   left_result = not(list_x[i] or list_y[j] or list_z[k])
   
   right_result = not list_x[i] and not list_y[j] and not list_z[k]
   if (left_result == right_result):
    print(left_result, '=', right_result, 'True')
   else:
           print(left_result, right_result,'False')
print()     