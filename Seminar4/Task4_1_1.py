#Вычислить число c заданной точностью *d*
#Пример:
#при d = 0.001, π = 3.141
#при d = 0.1, π = 3.1
#при d = 0.00001, π = 3.14154
# от 0.1 до 0.0000000001



k = 1
x = 0
for k in range(1, 4000000):
            x = x+4*((-1)**(k+1))/(2*k-1)



d=(input('Введите точность для вычисления числа Pi: '))
if (float(d)>0.1 or float(d)<0.0000000001):
    print("Введенное число некорректно")
else:
        r=len(str(d))-2
        print(round(x,r))