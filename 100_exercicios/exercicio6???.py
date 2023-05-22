#Escreva um programa que receba um número inteiro do usuário
#  e verifique se ele é um número perfeito. 
# Um número perfeito é aquele que é igual à soma de seus divisores, 
# excluindo ele mesmo. O programa deve exibir "É um número perfeito" ou 
# "Não é um número perfeito" de acordo com o resultado.

num = int(input('Digite um numero:  '))
count = 0

for c in range (1, num , 1):
    count += c
    if num % c == 0:
        print()

   
       