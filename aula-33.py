# Atribuição condicional

#Atribuição condicional é uma estrutura utilizada para simplificar o código, onde o valor a ser atribuido será aquele que satisfizer a condição.

"""
<variável> = <valor1> if(true) else <valor2>
var = 10 if (True) else 20 
"""

'''
>>> x = 10
>>> texto = 'sim' if x == 10 else 'não'
>>> texto
'''

num1 = int(input('Digite um número: '))
s = 'par' if num1 % 2 == 0 else 'ímpar '
#explicação da expressão a cima 
#o valor atribuido a variável 's' vai depender se o valor atribuido a variável 'num1' for dividido por 2 e a sobra for o valor 0 
# se o valor for dividido por 2 e não sobra nada ele vai atribuir a string 'par' a variável 's' se não vai atribuir a string 'ímpar' a variável 's'.
 
print('o número digitado é ', s)

