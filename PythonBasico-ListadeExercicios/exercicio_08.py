# Classificação de Nota

# Informar nota de 0 a 10.
# Caso a nota for 10: Excelente.
# Se for 8 ou 9: Muito bom.
# Se for 6 ou 7: Regular.
# Caso ao contrário, se for abaixo de 6: Insuficiente.

nota = int(input('Informe sua nota de 0 a 10: '))

match nota:
    case 10:
        print(f'Sua nota é {nota}. Excelente!')
    case 8 | 9:
        print(f'Sua nota é {nota}. Muito bom!')
    case 6 | 7:
        print(f'Sua nota é {nota}. Regular!')
    case _:
        print(f'Sua nota é {nota}. Insuficiente!')