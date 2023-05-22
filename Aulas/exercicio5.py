#Faça um programa que peça o nome do usuário e verifique se ele é "admin", 
# ele é admin ser for Lucas ou Pedro.

name = input('Diga seu nome: ').lower()

if name == 'lucas' or name == 'pedro':
    print('Voce é um ADMIN')
else : 
    print('Voce nao é um admnistrador')
    