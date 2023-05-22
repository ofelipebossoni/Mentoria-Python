# Numeros 
# Pyhton possui dois tipos de numero Inteiro e Float(Numeros Quebrados com casas decimais)
2 + 1 # Soma 
2 - 1 # Subtracao
2 * 2 # Multiplicacao
2 / 2 # Divisao
3 ** 2 # elevar numero
4 ** (1/2) # Raiz Quadrada

# Variaveis
# São caxinhas que gravam valores a certa variavel
# nomeas de variaveis nao podem comecar com numero, nao pode haver espacos no nome dad variaveis
# Usar apenas o _ para dividir nome da variavel e usar apenas letras minusculas
# podemos atualizar o valor da variavel, e usar a mesma para fazer contas ou atribuicoes
a = 5
b = 3
variavel_1 = a + b 
variavel_1 
a = a ** 3 # Atribuicao e mudanca de valor da varialve
a

# Strings 
# Forma do computador manipular textos
# pode usar aspas simples ou asplas duplas porem se comecar com uma tem que terminar com a mesma
# palavras reservada pelo python que ja possuem uma funcao nao podem ser usadas como variavel
# strings podem ser usadas em soma nao do valores mas agrupacao de uma string com outra
# podemos acessar os espacos dentro de uma string

minha_string = 'Isso é uma string'
minha_string

# len funciona para calcular o tamanho de espacos dentro de uma string 

len(minha_string)

# acessando dados da string, lembrando que a contagem comeca em 0

minha_string[3]

minha_string[:] # retornar todas as valores da string

minha_string[:] # primeira valor incluido segundo valor retira o elemento acionado
minha_string[0:14] # retira os items acionados da string
minha_string[1:16]
minha_string[:-5] # retira espacos da string de tras para frente
minha_string[-5] # retorna um valor especifico da string de tras para frente
minha_string[::2] # pula a string de 2 em 2
minha_string[::-1] # inverte a string 
'minha_string' * 2 # modelo para multiplicar uma string 
type('minha_string') # para sabermos o tipo da string
minha_string1 = 2

dir(minha_string) # mostra os metodos que podemos colocar na string
minha_string.lower() # transforma a string em minuscula
minha_string.upper() # transforma a string em maiscula
minha_string.split() # se usado sem argumento transforma string em uma lista
teste_string = 'felipe bossoni'
teste_string.split()
teste_string.split('o') # retira um espaco da string
dir('felipe bossoni')
'felipe bossoni'.capitalize() # retorna a primeira letra maiscula 
'felipe bossoni'.count('l') # precisa de um argumento e conta quantos argumentos tem na string
'felipe bossoni'.endswith('o') # retorna se o ultimo espaco da string finaliza com o argumento 
'felipe bossoni'.find('o') # mostra em qual espaco da string o argumento se encontra
'4'.isalnum() # pergunta se a string é toda numerica, retorna true or false 
'felipe bossoni'.index('o') # praticamente igual o count
'felipe bossoni'.replace('o', 'a') # retira um espaco do argumento e coloca outro no lugar
idade = 29
'felipe bossoni tem : {}'.format(idade) # recebe uma variavel 
ajuda = 'ola'
ajuda[0:3]*2

'eu tenho 20 anos'.split()

# Listas espacos na memoria que recebem alguma variavel
# comeca com colchetes e dividimos os items da lista por virgula
# podemos acessar os valores da lista assim como acessamos os espacos nas strings
# podemos usar qualquer elemento dentro da lista
# contagem da esquerda para direita sempre comeca no "0"
minha_lista = [1, 2 ,3]
type(minha_lista) 
minha_lista[-1]
minha_lista [:] 
minha_lista[0:-1] 
minha_lista[::-1]
modelo_lista = [1,2, "felipe", 3, [7,2,9,32]]
modelo_lista[4] #podemos acessar qualquer dado da lista porem temos que alinhar ele como cada um como elemento
modelo_lista[2].upper()
modelo_lista[2].replace('e', 'i')
modelo_lista[4][2]
l = [1, 2, 3]
l.append(2) # acrescenta um valor na lista
l
l.pop(1) # Retira o ultimo valor da lista e retorna o valor retirado
minha_lista.pop()
minha_lista
minha_lista.append(3)
minha_lista
modelo_lista[4].sort() # coloca em ordem uma lista 
modelo_lista[4].reverse() # coloca de forma inversa os valores da lista

t_lista = [1, 2, 3]
t_lista2 = [4, 5, 6]
t_lista3 = [7, 8, 9]
full_list = [t_lista, t_lista2, t_lista3] # alinhando listas dentro de lista
# de qualquer forma que estiver conseguimos acessar qualquer dado da lista [] primeiro serve para acessar a lista em questao, [] segundo serve para acessar os dados da lista
list_ex = [1, 2, 'Maria', 'Joao', 3,[1,2,3]]
list_ex[3:]

# Dicionarios 

# manipula e armazena dados, porem podemos armazenar pares da dados no dicionario
# key = Chave identificador do valor | values = Valor associado a chave
# podemos criar chaves depois no dicionario e colocar um valor atrelado a ele.

meu_dic = {'nome': 'felipe', 'idade' : 29, 'filhos' : ['Antonio','Francisco']}
meu_dic['nome']
meu_dic['filhos']
meu_dic.keys() # retorna todas as chaves do dicionario em questao
meu_dic.values() # retorna os valores associados as chaves do dicionario
meu_dic.items() # retorna em formato de tuplas os valores e chaves do dicionario
meu_dic.popitem() # retira a ultima chave e valor do dicionario
meu_dic.clear() # limpa tudo do dicionario
meu_dic.setdefault('filhos')
meu_dic.pop('idade') # retira um item especifico declarado
meu_dic['Cidade'] = 'Maringa'
meu_dic['Profissao'] = ['Empresario', 'Programador']
meu_dic.values()

# Tuplas
# funcionam como as listas porem elas sao imutaveis, no meio do caminho nao podemos alterar valores
# Sao legais para colocarmos em programas aonde nao queremos alterar os dados
# Servem para podermos declarar mais de uma varualvel de uma vez
tupla = (1, 2, 3)
tupla
tupla[0]
# exemplo despacotamento de Tuplas
tu, tup, fel, jr = (1, 2, 3, 7)
completa = (tu + fel + jr)  
completa
a, b , c, v = ('felipe', 'debora', 'Francisco', 'Antonio')
a
v

# Inputs
# input é uma funcao do python que conseguimos pegar valores do usuario
# float recebe um dado quebrado e int numero inteiro

nome = input()
idade = int(input())
conta = float(input())

# Set
# funcionam como uma lista porem ele nao guarda valores repetidos
# Quando o valor é atualizado o mesmo é posto em ordem
# podemos colocar uma lista dentro de um set e ele coloca em ordem e elimina os valores repetidos

x = set()
x.add(1)
x.add(1)
x.add(4)
x.add(3)
x
a = [1, 2, 8 ,5, 7, 1, 2]
set(a)
x.union(a) # uniao de dois valores sendo puxadas pelo set 
x.intersection(a) # volta os valores em comun das duas variaveis 
x.difference(a) # valores que sao diferentes entre as duas listas
x.discard(1) # discarta um valor especificado 
x

# Boleano
# retorna se algo é verdadeiro ou falso

a = 2
b = 7
type(a > b)

# Operadores de Comperacao
# perguntas que obtemos como resposta false ou true

2 == 2 # igualdade
a = 2 # atribuindo um valor a variaves
2 != 1 # desigualdade pergunta se algo é diferente da outra se for verdade retorna true se for mentira retorna false
2 > 1 # volta se um item é maior que o outro
2 >= 2 # maior ou igual
2 <= 3 # menor ou igual.

# operadores de comparacao em cadeia 
# AND funciona como e , se houver trade E tuver perna maior de 200 pontos (duas coisas precisam acontecer)
2 > 1 and 2 > 0  
# OR funciona como ou , se uma das afirmacoes for verdadeira ele retorna true
2 < 1 or 2 > 1 

#Estrtuturas de cointrole de fluxo
# funcionam como caminhos que o programa vai seguir se uma condicao for atendida
# fazemos uma pergunta ao computador conforme ele retorna algo tal caminho sera seguido
# IF se algo acontecer siga esse caminho

print('Qual a temperatura hoje:')
temp = float(input())

if temp >= 20 and temp <= 35:
    print('A temperatura esta otima')
elif temp > 35:
    print('Esta calor')
else :
    print('Esta frio')

# range 
# gera uma sequencia de variaveis
# funciona como uma caixa que guarda dados porem so abre quando chamamos ele
# funciona com numeros inteiros
# comeca a contagem no 0 
list(range(11))

# FOR (para) estrtura de laço
# para executar uma sequencia quantas vezes determinar








