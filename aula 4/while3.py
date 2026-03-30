usuario = ''
senha = ''
while (usuario != 'Mateus' or senha != '1234'):
    usuario = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

print('Bem-vindo ao novo mundo')


usuario = ''
senha = ''
while not (usuario == 'Mateus' and senha == '1234'):
    usuario = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

print('Bem-vindo ao novo mundo')