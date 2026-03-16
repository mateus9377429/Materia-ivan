titulo = input('Digite o nome do filme: ')
diaria = int(input('Por quantos dias você alugou o filme: '))
tempo = int(input('Por quantos dias ficou com filme: '))

valor = tempo * 5
multa = 0

if tempo - diaria > 0:
    multa = 15

total = valor + multa

print(f'valor a ser pago {total}')