#Iterando listas em Python

lista_nums = [100 ,200 ,300 ,400]
for item in lista_nums:
    print(item)

lista_nums = [100, 200, 300, 400]
lista_indice = [0, 1, 2 ,3 ]
for item in lista_indice:
    lista_nums[item] += 1000 
print(lista_nums)
