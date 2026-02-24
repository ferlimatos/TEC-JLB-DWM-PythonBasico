# Histórico de Tentativas

# Pedir entrada do usuário 5 vezes
# Criar a lista depois do usuário digitar 5 vezes
# Mostrar todos os números

numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(numero)

print('\nNúmeros digitados:')
for numero in numeros:
    print(numero)