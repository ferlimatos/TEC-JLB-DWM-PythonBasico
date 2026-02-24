# Dia da Semana

dia_semana = int(input('Informe um número de 1 a 7: '))

match dia_semana:
    case 1:
        print('Hoje é Domingo.')
    case 2:
        print('Hoje é Segunda-feira.')
    case 3:
        print('Hoje é Terça-feira.')
    case 4:
        print('Hoje é Quarta-feira.')
    case 5:
        print('Hoje é Quinta-feira.')
    case 6:
        print('Hoje é Sexta-feira')
    case 7:
        print('Hoje é Sábado.')
    case _:
        print('Esse número não corresponde a nenhum dia da semana.')