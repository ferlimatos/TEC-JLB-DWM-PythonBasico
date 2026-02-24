# Sistema de Pedidos

print("""Digite um comando para pedir uma comida:
1 - Hambúrguer
2 - Pizza
3 - Refrigerante""")
pedido = int(input('Comando: '))

match pedido:
    case 1:
        print('Eu quero um hambúrguer!')
    case 2:
        print('Eu quero um pizza!')
    case 3:
        print('Eu quero um refrigerante!')