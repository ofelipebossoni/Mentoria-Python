#Um banco quer um sistema para percorrer 
# a lista de transações de um cliente e calcular o saldo da conta.
#transacoes = [100, -50, 300, -200, 50]

saldo = [100, -50, 300, -200, 50]
cont = 0
for s in saldo:
    cont += s
print(f'Seu saldo é {cont}')