#Verificar se o produto tem desconto e qual é o valor final
# produto maior igual a 100 reais tem 10%
# produto maior igual a 50 reais tem 5%

produto1, preco1 = ('Apple Watch', 900.00)
produto2, preco2 = ('Aipods', 79.99)
produto3, preco3 = ('Mouse Pad', 19.99)

esc = int(input( f'Escolha seu produto \n 1 - {produto1}. \n 2 - {produto2}. \n 3 - {produto3}.\n'))

if esc == 1:
    print(f'O valor do seu {produto1} é de R$ {preco1 * 0.9} com 10% de desconto')
elif esc == 2:
    print(f'O valor do seu {produto2} é de R$ {preco2 / 0.95} com 5% de desconto')
elif esc == 3:
    print(f'O valor do seu {produto3} é de R$ {preco3}')
      


