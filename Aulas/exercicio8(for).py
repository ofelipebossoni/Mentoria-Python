#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
#usuário. Ex.: 5!=5.4.3.2.1=120



num = int(input('Digite um numero para ver o fatorial: '))
fatorial = 1
for c in range(num,1,-1):
    fatorial *= c
print(f'O fatorial do {num} é {fatorial}')

