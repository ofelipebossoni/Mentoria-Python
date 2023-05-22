#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
# Álcool: até 20 litros, desconto de 3% por litro |  acima de 20 litros, esconto de 5% por litro 
# Gasolina: até 20 litros, desconto de 4% por litro | acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro 
# da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina = 2.50
alcool = 1.90

print('Bem vindo a CENTRAL DE COMBUSTIVEL')
esc_comb = int(input('Qual combustivel voce precisa : 1 para Alcool | 2 para Gasolina : \n'))

if esc_comb == 1 or esc_comb == 2 :
    lit = float(input('Quantos litros voce vai precisar: \n'))
    
    if esc_comb == 1 and lit <= 20:
        desc_alcool = (lit * alcool) * 0.97 
        print(f'Comb escolhido: Alcool | Litragem | : {lit} | Valor total a seu pago : {desc_alcool:.2f}')
    elif esc_comb == 1 and lit > 20:
        desc_alcool2 = (lit * alcool) * 0.95
        print(f'Comb escolhido: Alcool | Litragem | : {lit} | Valor total a seu pago : {desc_alcool2:.2f}')
    elif esc_comb == 2 and lit <= 20:
        desc_gasolina = (lit * gasolina) * 0.96 
        print(f'Comb escolhido: Gasolina | Litragem | : {lit} | Valor total a seu pago : {desc_gasolina:.2f}')
    elif esc_comb == 2 and lit > 20:
        desc_gasolina2 = (lit * gasolina) * 0.94 
        print(f'Comb escolhido: Gasolina | Litragem | : {lit} | Valor total a seu pago : {desc_gasolina2:.2f}') 

elif esc_comb == 0 or esc_comb > 2 :
    print('Escolha uma opcao valida: 1 para Alcool | 2 para Gasolina')







