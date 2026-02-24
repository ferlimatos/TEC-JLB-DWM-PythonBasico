# Média de Lista

notas = [7,8,9,6,10]

soma_total = 0

for n in notas:
    soma_total += n

quantidade = len(notas)
media = soma_total / quantidade

print(f"A soma das notas é: {soma_total}")
print(f'A média final é: {media}.')