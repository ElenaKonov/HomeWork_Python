#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc






with open('Text1.txt', 'r') as f:
    dataString=f.read()
f.close()

##print(dataString)


dict={}


for letter  in dataString:
        if dict.get(letter):
            dict[letter]=dict.get(letter)+1  
        else:
            dict[letter]=1        





result=''
for i  in dict.items():
        result=result+str(i[1])+i[0]


with open('file_result1.txt', 'w') as f:
    f.write(result)
       
 
 
with open('Text2.txt', 'r') as f:
    dataString=f.read()
f.close()

#print(dataString)







num_list = []
 
num = ''
for simbol in dataString:
    if simbol.isdigit():
        num = num + simbol
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
 



letter_list = []
 
letter = ''
for simbol in dataString:
    if simbol.isalpha():
        letter = letter + simbol
    else:
        if letter != '':
            letter_list.append(letter)
            letter = ''
if letter != '':
 letter_list.append(letter)
 

result2=''
for i in range(len(num_list)):
        for j in range(0,num_list[i]):
                   result2=result2+letter_list[i]
                  





with open('file_result2.txt', 'w') as f:
    f.write(result2)
       

 



