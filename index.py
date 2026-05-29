def linha():                                            #função que gera uma linha para melhor organização visual
    print('-'*40)

def menu():                                             #função que exibe um menu para o usuário e retorna a opção escolhida
    linha()
    print('Escolha entre as opções abaixo:')
    print('1 - ')
    print('2 - ')
    print('3 - ')
    print('4 - ')
    print('5 - Encerrar o programa')
    opc = input('Digite sua escolha: ')                 #variável local que representa a escolha do usuário
    linha()
    return opc

while True:                                             #loop para manter o programa rodando até que o usuário escolha encerrar
    op = menu()                                         #variável global que representa a escolha do usuário
    match op:
        case '1':
            print('Opção 1 escolhida')
        case '2':
            print('Opção 2 escolhida')
        case '3':
            print('Opção 3 escolhida')
        case '4':
            print('Opção 4 escolhida')
        case '5':
            break
        case _:
            print('Por favor, digite uma opção válida')
            print('Você deve digitar o número que represente sua escolha')