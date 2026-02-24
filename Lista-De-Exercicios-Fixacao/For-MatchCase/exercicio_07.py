# Menu Simples

cadastro_lista = []

while True:

    print("""Digite um número para navegar no menu:
1 - Cadastrar
2 - Listar
3 - Sair""")
    comando = int(input('Comando: '))

    match comando:
        case 1:
            cadastro = input('Digite o nome do cadastro: ')
            cadastro_lista.append(cadastro)
            print('Nome cadastrado com sucesso.')
        case 2:
            print('Listando nomes cadastrados...')
            if cadastro_lista:
                for nome in cadastro_lista:
                    print(nome)
            else:
                print('Nenhum nome cadastrado.')
        case 3:
            print('Saindo do menu.')
            break
        case _:
            print('Opção inválida.')