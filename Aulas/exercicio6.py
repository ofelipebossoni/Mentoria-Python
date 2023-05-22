#Verificar se o usuário digitou o login e a senha corretos 
#usuario = miveiga
#senha = 12345!

usuario = input('Digite seu usuario : ').lower()
senha = input('Digite sua senha : ').lower()

if usuario == 'miveiga' and senha == '12345!':
    print('Usuario logado com sucesso!')
else :
    print('Usuario ou senha incorretos')