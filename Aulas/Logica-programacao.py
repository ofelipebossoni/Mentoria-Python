# Logica da programaca, nada mais é que uma receita um algoritmo que escrevemos para dizer ao computador oque ele tem que fazer.

# computadores são totalmente literais ele fazem exatamente oque mandamos, por isso precisamos descrever bem o caminho que ele deve seguir

# algoritmo é um conjunto de passos finitos e organizados, que quando executados, resolvem determinado problema.

# MODELO algoritmo de compra

print('Vá ate a geladeira =====>')
print('abra a geladeira.')
print('Olhe na segunda prateleira se há ovos')
print('quantos ovos voe esta vendo?')
n_ovo = int(input())
if n_ovo == 0:
    print('Vá ate a mesa, pegue sua carteira e vá no mercado comprar mais ovos.')
elif n_ovo > 1:
    print('Não precisa comprar ovos')

# MODELO algoritmo pure de batatas

print('Abrir a geladeira.Quantas batatas voce tem?')
cont_batata = int(input())
print('Voce possui {}, batatas'.format(cont_batata))
receita = 6 
if cont_batata > 6 :
    print('Voce nao precisa comprar batatas')
elif cont_batata < 6 :
    print('Voce precisa comprar : {} batatas'.format(receita - cont_batata))

# Todo algoritmo segue a seguinte padrao entrada > processamento  > saida. Lembrando que algoritmos servem para resolucao de um problema.

# Modelo calculo media notas 

# Afirmacoes sobre algoritmos
# 1 - Algoritmo é um conjunto de passos finitos e organizados que quando executados resolvem um problema
# 2 - Para se resolver algo passos precisam ser tracados (1 - Entrada | 2 - processamento | 3 -  Saida)

# Elementos basicos que constituem um programa : 
# 1 - Variaveis 
# 2 - Constantes
# 3 - Operadores
# 4 - Estruturas de controle de fluxo
# 5 - Laços 
# 6 - Metodos

# Variaveis e Constantes 
# São elementos basicos que um programa manipula. Uma variavel é um espaco reservado na memoria do computador para armazenar um tipo de dado determinado. 
# Embora uma variavel possa assumir diferentes valores, ela so pode armazenar um valor a cada instante 
# podem ser de 4 tipo :  Numericas, caracteres, alfanumericas e logicas 
# numericas  = 1, 2, 3, 4 
# caracteres = felipe, francisco, debora, antonio
# alfanumericas = felipe227856
# logicas = false - true = verdadeiro ou falso

# Operadores = são a forma de manipular elementos, operadores retornan algum resultado
# Operadores numericos, apenas para numeros (+) - (-) - (*) - (/) - (**)exponenciacao 
# Operadores Relacionados = (=) (<>) (>) (<) (>=) (<=), resposta desse operador é sempre true ou false 
# Operador logico = (and) (or) (not)
# Estruturas de controle de Fluxo = (if) elemento para tomada de decisao de um caminho a ser tracado
# Estruturas de repeticao = se determinada condicao for verdadeira ela continua repetindo a acao ate a resposta mudar (while)


    