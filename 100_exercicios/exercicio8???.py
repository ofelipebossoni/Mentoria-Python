#Escreva um programa que receba o valor total da compra 
# e o valor pago pelo cliente e calcule o troco a ser dado. 
# Considere apenas notas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2. O programa deve exibir 
# a quantidade de notas de cada valor que devem ser entregues.

val1 = int(input('Valor da compra: '))
val = int(input('Valor recebido: '))
troco = val1 - val
ced = 100
tot_ced = 0

while True:
    if troco >= ced:
        troco -= ced
        tot_ced += 1






