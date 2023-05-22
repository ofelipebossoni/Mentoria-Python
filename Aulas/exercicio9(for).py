#Um aplicativo pode usar um laço de repetição "for" 
#para percorrer a lista de usuários e enviar uma notificação para cada um.
#usuarios = ['Ana', 'João', 'Pedro', 'Maria']

users = ['Ana', 'João', 'Pedro', 'Maria']
users_2 = ['Ana', 'João', 'Pedro', 'Maria', 'paulo', 'alex', 'debora', 'antonio']

for notif in users_2:
    print(f'ola {notif}')
