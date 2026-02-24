# Contador de Vogais

# Início do programa

vogais = "aeiou"
contador = 0

palavra = input('Digite uma palavra: ').lower() # Pedir uma palavra para o usuário
print(f'A palavra digitada é: {palavra}')

for letra in palavra:
    if letra in vogais: # Verificar se há vogal na palavra
        contador += 1

if contador > 0:
    print(f'A palavra contém {contador} vogais.') # Se houver, irá contar quantas vogais tem na palavra.
else:
    print('Não há vogais na palavra.') # Se não houver, irá informar que não há vogais na palavra.

# Fim do programa






