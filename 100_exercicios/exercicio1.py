#Escreva um programa que receba uma palavra do 
# usuário e verifique se ela é um palíndromo, ou seja, 
# se pode ser lida da mesma forma de trás para frente. O programa deve exibir 
# "É um palíndromo" ou "Não é um palíndromo" de acordo com o resultado.

word = input('Digite uma palavra: \n').upper()
palin = word[::-1]

if palin == word:
    print('É palindromo')
else :
    print('Não é palindromo')