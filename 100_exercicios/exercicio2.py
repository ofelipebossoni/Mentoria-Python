#Escreva um programa que receba as notas e pesos de 5 provas de um aluno e calcule a média 
# ponderada dessas notas. O programa deve exibir a média final.

peso1 = 5
peso2 = 16
peso3 = 3
peso4 = 1
peso5 = 5
full_peso = (peso1+peso2+peso3+peso4+peso5)

nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))
nota3 = float(input('Digite sua 3º nota: '))
nota4 = float(input('Digite sua 4º nota: '))
nota5 = float(input('Digite sua 5º nota: '))

media = ((peso1 * nota1)+(peso2 * nota2)+(peso3 * nota3)+(peso4 * nota4)(peso5 * nota5))/ full_peso

print('Sua media final é {:.2f}'.format(media))    




