# Cálculo do desconto em uma loja
# Uma loja está oferecendo um desconto progressivo 
# com base no valor total da compra. 
# Escreva um programa que receba o valor total da compra 
# e aplique o desconto de acordo com a tabela abaixo. 
# O programa deve exibir o valor final a ser pago.

#Tabela de desconto:
#Valor total da compra:

#Até R$ 100: sem desconto
#De R$ 100 a R$ 500: 5% de desconto
#Acima de R$ 500: 10% de desconto

v_compra = float(input('Digite o valor total da compra: \n'))

if v_compra <= 100:
    print(f'O total da compra vai dar {v_compra:.2f}')
elif v_compra <= 500:
    des1 = v_compra * 0.95
    print(f'O total deu R$ {des1:.2f} reais.')
else :
    des2 = v_compra * 0.90
    print(f'O total deu R$ {des2:.2f} reias.') 
