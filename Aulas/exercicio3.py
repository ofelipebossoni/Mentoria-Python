#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" 
# "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como inocente

print('responda 0 para SIM | 1 para nao')

question1 = int(input('Telefonou para a vitima?'))
question2 = int(input('Esteve no local do crime?'))
question3 = int(input('Mora perto da vítima?'))
question4 = int(input('Devia para a vítima?'))
question5 = int(input('Já trabalhou com a vítima?'))
part_crime = (question1 + question2 + question3 + question4 + question5 )

if part_crime > 5 or  part_crime < 0 :
    print('\2Digite um valor valido apenas 0 ou 1')
elif part_crime == 5:
        print('Assasino.')
elif part_crime == 3 or part_crime == 4:
        print('Cumplice')
elif part_crime == 2:
        print('Suspeita')
elif part_crime == 0 :
        print('Inocente')
