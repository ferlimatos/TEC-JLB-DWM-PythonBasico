# Maior Número da Lista

numeros = [10,25,7,89,34]

numero_maior = numeros[0]

for n in numeros:
    if n > numero_maior:
        numero_maior = n

print(f'O maior número da lista é: {numero_maior}')