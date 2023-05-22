#Um e-commerce quer um sistema
# para percorrer a lista de produtos em promoção 
# e exibir uma mensagem de desconto para cada um.
#produtos_promocao = ['Camiseta', 'Calça', 'Tênis']
#percentual_desconto = 20

produtos_promocao = [('Camiseta', 78.99), ('Calça', 89.77), ('Tênis', 29.99)]

for prom in produtos_promocao:
    print(f'Nao perca a promocao de {prom[1]} por {prom[1]* 0.80:.2f} reais')