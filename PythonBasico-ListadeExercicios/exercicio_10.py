# Verificação de Comando

print("""Escolha e digite um comando:
iniciar
pausar
parar""")
comando = (input('Comando: ')).lower()

match comando:
    case "iniciar":
        print('Iniciando o programa...')
    case "pausar":
        print('Pausando o programa...')
    case "parar":
        print('Parando o programa...')