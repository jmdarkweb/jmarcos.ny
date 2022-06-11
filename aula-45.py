#Curso de Python - Aula 45 - Class List II - eXcript

print()
lista1 = ['a', 3]
print(lista1)
lista = [['a', 'b', 'c'], [5, 8, 2], []] #pode conter lista dentro da nossa lista 
print(lista)

print(lista[0]) # para passar o primeiro elemento da lista, ou a primeira lista dentro da lista.

# a função length retorna o conprimento da nossa lista 
# mas só precisamos digitar len 
len(lista) 
# assim nós veremos que a nossa lista só tem 3 elementos 
print('O número de elementos na lista é', len(lista))
if(len(lista)<=3):
    print('menor que 3')
    print(lista[0])

else:
    print('maior que 3')


