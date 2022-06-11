Curso de Python - Aula 46 - Listas III - eXcript

"""
>>> lista = [1,2,3,4,5]                                   │
>>> lista                                                 │
[1, 2, 3, 4, 5]                                           │
>>> len(lista)                                            │
5                                                         │
>>> lista = lista + [6]                                   │
# se vc quiser colocar o valor no final da lista vc coloca o valor no final, como a cima
>>> lista                                                 │
[1, 2, 3, 4, 5, 6]                                        │
>>> lista = [0] + lista                                   │
# se vc quiser colocar o valor no começo da lista vc colocar o valor no começo, antes da variavel lista, como está a cima.
>>> lista                                                 │
[0, 1, 2, 3, 4, 5, 6]                                     │

#outra maneira que vc pode adicionar valor a lista é com a função 'append()'

>>> lista.append(11)                                      │
#olha o exemplo acima
>>> lista                                                 │
[0, 1, 2, 3, 4, 5, 6, 11]                                 │

# e para excluir um item da lista é só usar a função 'del'
>>> del(lista[-1])                                        │
# como no exemplo acima 
>>> lista                                                 │
[0, 1, 2, 3, 4, 5, 6]                                     │
>>> 10*[0]                                                │
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]                            │
>>> lista += 10*[0]                                       │
>>> lista                                                 │
[0, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]       │
>>>                                                      │
      

"""

