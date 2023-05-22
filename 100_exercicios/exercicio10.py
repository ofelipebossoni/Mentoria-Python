#Verificação de número de telefone válido 
# Escreva um programa que receba um número de 
# telefone do usuário e verifique se ele é válido.
# Considere o formato (XX) XXXX-XXXX, onde X é um dígito. 
# O programa deve exibir "Número de telefone válido" ou 
# "Número de telefone inválido" de acordo com o resultado.

tel = input('Digite seu telefone com o codigo do estado : \n')
qnt = len(tel)

if qnt == 10:
    print('Numero de telefone valido')
else :
    print('Numero de telefone invalido')