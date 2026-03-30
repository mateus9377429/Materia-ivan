# estrutura de repetição: while

while True:
    usuario = input('Digite seu login: ')
    senha = int(input('Digite sua senha: '))

    if (usuario == 'admin' and senha == 123):
        break
    else:
        print('Falha')

print(f'Seja bem-vindo ao novo mundo {usuario}')