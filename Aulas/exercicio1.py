#Faça um Programa que verifique se uma letra digitada é vogal ou consoante
# \n para quebrar linha, pode ser colocado em qualquer local da string
a = input('Digite uma letra para saber se é vogal ou consoante: \n ').lower()
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('É Vogal.')
else:
    print('É consoante')

