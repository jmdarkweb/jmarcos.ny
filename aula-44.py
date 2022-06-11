#Curso de Python - Aula 44 - Cass List I - eXcript
'''
>>> lista = [1, 2, 8, 5, 15, 3, 6, 8]
>>> lista
[1, 2, 8, 5, 15, 3, 6, 8]
>>> ['ffa', 3, 'dsf']
['ffa', 3, 'dsf']
>>> type(['ffa', 3, 'dsf'])
<class 'list'>
>>> type([]) #tudo que estiver dentro de [] é uma lista (do tipo lista)  
<class 'list'>
>>> lista[0] #O primeiro elemento da lista é o número um
1
>>> lista[1] #O segundo elemento da lista do tipo 'list' é o número 2
2
>>> lista[5] #O sexto elemento da lista do tipo 'list' é o número 3
3
>>> lista[1]+lista[2] # A soma do valor do segundo elemento da lista, com o terceiro elemento da lista 
10
>>> l = ['a', 'b', 'c', 'd', 'e']
>>> l
['a', 'b', 'c', 'd', 'e']
>>> l[0]
'a'
>>> l[3]
'd'
>>> lista = list("eXcript") #Tudo que é declarado no python entre " é uma 'string'
>>> lista # cada elemento da string será uma parte da lista que foi declarada como variável 
['e', 'X', 'c', 'r', 'i', 'p', 't'] 
>>> lista = list((4, 5, 8))
>>> lista 
[4, 5, 8]
>>> lista = list(("eXcript"))
>>> lista  # não da certo porque em lista e em tuplas para nós diferenciarmos um elemento de um objeto interavel, nós deveremos colocar uma virgula após o elemento 
['e', 'X', 'c', 'r', 'i', 'p', 't']
>>> lista = list(("eXcript",)) # Desse jeito
>>> lista 
['eXcript']
>>> ['aaaf', 'fsdadfsd', 3 , 8,]
['aaaf', 'fsdadfsd', 3, 8]
>>> a = (5) # essa variável do tipo inteiro 
>>> type(a)
<class 'int'>
>>> a = (5,) # mas se vc declarar assim ela será do tipo tupla, o python vai consegui distingui por causa da , 
>>> a
(5,)
>>> type(a) # o python ira interpreta a virgura como se tivesse uma continuação, e assim vai interpreta como sendo do tipo tupla.
<class 'tuple'>
>>> 
     
'''
print("eXcript")
