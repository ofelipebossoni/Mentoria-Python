#Escreva um programa que gere e exiba os primeiros 20 números da sequência de Fibonacci.
# sequenci ade fibonacci é o resultado da soma dos dois ultimos numeros da sequencia.

count1 = 0
count2 = 1
count = 1
print(1)
for i in range(20):
    print(count)
    count1 = count2
    count2 = count
    count = count1 + count2
    