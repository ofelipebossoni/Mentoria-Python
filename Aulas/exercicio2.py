#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar: 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# A mensagem "Reprovado", se a média for menor do que sete; 
# A mensagem "Aprovado com Louvor", se a média for igual a dez.

nota1 = float(input('Digite sua primeira nota: \n '))
nota2 = float(input('Digite sua segunda nota: \n '))
cal_media = (nota1 + nota2) / 2

if cal_media == 10:
    print(f'Aprovado com louvor! {cal_media}.')
elif cal_media >= 7:
    print(f'Aprovado! {cal_media}.')
else :
    print(f'Reprovado! {cal_media}.')
