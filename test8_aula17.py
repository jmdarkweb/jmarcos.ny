# curso de python aula 17 eXcript 
print(3%2) # para saber qual vai ser o resto dessa divisão: o restó é 1 
print(4%2) # para saber se tem resto de divisão: essa divisão não tem resto 

print(5%2) # resultado: 1
print(7%3.1) # resultado: 0.7999999999999998

# Mas para que precisaria saber o resto de uma divisão ?
# para saber se o número é pá ou se o numero é exato

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1/num2
resto = num1 % num2

print(num1, "dividido por", num2, "é igual a: ", divisao)
print("O resto da divisão entre", num1, "e", num2, " é igual", resto )
