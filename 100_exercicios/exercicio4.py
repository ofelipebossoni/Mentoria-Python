#Escreva um programa que receba um número inteiro do usuário e verifique 
# se ele é um número primo. O programa deve exibir "É um número primo" 
# ou "Não é um número primo" de acordo com o resultado.

num = int(input('digite um numero : '))
count = 0
for i in range(2, num):
    if num % i == 0:
        count == 1
        break
if count == 0:
    print('É primo')
else : 
    print('Não é primo')
 
    


