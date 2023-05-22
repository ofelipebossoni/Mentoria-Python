#Verificação de idade para venda de bebida alcoólica
#Um mercado precisa verificar se um cliente é maior de idade
#  para vender bebidas alcoólicas. Escreva um programa que receba 
# a idade do cliente e exiba "Pode vender" ou "Não pode vender" de acordo com o resultado.

id = int(input('Digite sua idade : '))

if id >= 18:
    print('Pode vender')
else:
    print('Não pode vender')