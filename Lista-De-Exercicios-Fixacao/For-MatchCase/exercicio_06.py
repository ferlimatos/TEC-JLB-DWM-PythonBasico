# Operações Matemáticas
from contextlib import nullcontext

print('Digite dois números: ')
numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))
operacao = input('Escolha uma operação (+, -, *, /): ')

resultado = None # a variável não possui nenhum valor

match operacao:
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        resultado = numero1 / numero2
    case _:
        print('Operação invalida!')

if resultado is not None:
    print(f'{numero1} {operacao} {numero2} = {resultado}')