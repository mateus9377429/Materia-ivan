import funcao

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

r = funcao.somar(numero1, numero2)

funcao.pularLinha()
funcao.imprimir(f'O valor da soma de {numero1} + {numero2} é {r}')  