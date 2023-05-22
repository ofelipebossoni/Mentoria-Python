#Escreva um programa que receba um número de CPF do usuário 
# e verifique se ele é válido. O programa deve exibir "CPF válido" 
# ou "CPF inválido" de acordo com o resultado.

cpf = input('Digite seu CPF : \n')
qnt = len(cpf)

if qnt == 11:
    print('Seu cpf é valido')
else :
    print('Seu CPF esta incorreto')

