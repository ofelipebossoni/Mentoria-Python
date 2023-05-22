#Uma clínica médica quer um sistema  para percorrer a lista de pacientes e exibir a idade de cada um.
#pacientes = [{'nome': 'Ana', 'idade': 35}, {'nome': 'João', 'idade': 42}, {'nome': 'Pedro', 'idade': 28}, {'nome': 'Maria', 'idade': 50}]

pacients = [{'nome': 'Ana', 'idade': 35},
            {'nome': 'João', 'idade': 42}, 
            {'nome': 'Pedro', 'idade': 28}, 
            {'nome': 'Maria', 'idade': 50}]

for c in pacients:
    print('{} idade {} anos'.format(c['nome'],c['idade']))