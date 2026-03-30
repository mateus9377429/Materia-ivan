while True:
    try:
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o Segundo numero: '))

        resultado = num1 / num2

        print(f'O resultado da divisão é {resultado}')
        break
    
    except ValueError as error:
        print('O valor digitado é invalido, digite novamente: ')
    
    except ZeroDivisionError as error:
        print('DIgite um valor maior que 0: ')
        
    except Exception as error:
        print('Ocorreu um erro: ', error)