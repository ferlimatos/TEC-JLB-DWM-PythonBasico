# Mini Menu Bancário

# Como o exercício não pede a necessidade de loop, o saldo será definido.
# O programa irá executar apenas uma opção.

saldo = 500.00

print("""Escolha um comando para executar em sua conta:
1 - Ver saldo
2 - Depositar
3 - Sacar
4 - Sair""")
comando = int(input('Comando: '))

match comando:
    case 1:
        print(f'Saldo da sua conta: R${saldo:.2f}')
    case 2:
        valor = float(input('Digite o valor para depósito: R$'))
        saldo += valor
        print(f'Depósito realizado com sucesso.')
        print(f'Novo saldo: R${saldo:.2f}')
    case 3:
        valor = float(input('Digite o valor para saque: R$'))
        if valor <= saldo:
            saldo -= valor
            print('Saque realizado com sucesso.')
            print(f'Novo saldo: R${saldo:.2f}')
        else:
            print('Saldo insuficiente!')
    case 4:
        print('Saindo da conta...')
    case _:
        print('Opção inválida.')