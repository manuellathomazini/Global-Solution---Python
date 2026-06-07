# --- Predefinições de variáveis globais e funções para o programa ---

def linha():                                                    #função que gera uma linha para melhor organização visual
    print('-'*40)

def menu():                                                     #função que exibe um menu para o usuário e retorna a opção escolhida
    linha()
    print('Escolha entre as opções abaixo:')
    print('1 - Conteúdo sobre a Síndrome de Kessler')
    print('2 - Solução OrbClear')
    print('3 - Quiz de conhecimento sobre a Síndrome de Kessler')
    print('4 - Seus Resultados')
    print('5 - Encerrar o programa')
    opc = input('Digite sua escolha: ')                         #variável local que representa a escolha do usuário
    linha()
    return opc

def validar(r):                                                 #função que valida a resposta do usuário, garantindo que seja uma das opções válidas
    r_validas = ['A', 'B', 'C', 'D']                            #respostas válidas para o quiz
    if r in r_validas:
        return True
    else:
        return False

def voltar():                                                   #função para retornar ao menu
    input('------| Pressione Enter para voltar para o Menu |------')

r_user = []                                                     #lista global para armazenar as respostas do usuário ao quiz
r_gabarito = ['B', 'C', 'B', 'A', 'D']                          #lista global que representa a ordem do gabarito do quiz

# --- Início do programa ---

while True:                                                     #loop para manter o programa rodando até que o usuário escolha encerrar
    op = menu()                                                 #variável global que representa a escolha do usuário
    match op:
        case '1':
            print('A Síndrome de Kessler é um cenário no qual o volume de lixo espacial na órbita baixa da Terra (LEO) se torna tão denso que colisões entre objetos geram uma reação em cadeia. Cada colisão cria milhares de novos fragmentos, resultando em um crescimento exponencial de detritos que torna a órbita inutilizável.')
            print('Isso pode representar um risco significativo para satélites, estações espaciais e futuras missões espaciais, além de dificultar o acesso ao espaço.')
            voltar()

        case '2':
            print('A solução OrbClear propõe o uso de um sistema de limpeza espacial que utiliza satélites equipados com tecnologia avançada para capturar, remover detritos espaciais em órbita e retornar para a Terra para reciclá-los. Esses satélites seriam capazes de identificar, rastrear e coletar os detritos, reduzindo assim o risco de colisões e contribuindo para a segurança espacial.')
            print('A OrbClear representa uma abordagem inovadora para enfrentar a síndrome de Kessler e garantir as operações espaciais no futuro, além de promover a sustentabilidade e a economia circular.')
            voltar()

        case '3':
            r_user.clear()                                        #reseta as respostas do usuário
            print('QUIZ: Agora você vai responder a um teste de 5 perguntinhas sobre a síndrome de Kessler!')

            # Questão 1

            linha()
            print('1. O que é a Síndrome de Kessler?')
            print('A) Um defeito em foguetes durante o lançamento.')
            print('B) Um efeito em que colisões espaciais geram mais detritos, causando novas colisões.')
            print('C) Uma falha em satélites de comunicação.')
            print('D) Um fenômeno climático da atmosfera terrestre.')
            resposta = input('Digite a letra da sua resposta: ').upper()
            while not validar(resposta):        #validação resposta
                resposta = input('Digite uma resposta válida (A / B / C / D): ').upper()
                if validar(resposta):
                    break
            r_user.append(resposta)

            # Questão 2

            linha()
            print('2. O que pode causar a Síndrome de Kessler?')
            print('A) Tempestades na Terra.')
            print('B) Excesso de astronautas em órbita.')
            print('C) Colisões entre satélites e detritos espaciais.')
            print('D) Falta de combustível nos satélites.')
            resposta = input('Digite a letra da sua resposta: ').upper()
            while not validar(resposta):
                resposta = input('Digite uma resposta válida (A / B / C / D): ').upper()
                if validar(resposta):
                    break
            r_user.append(resposta)

            # Questão 3

            linha()
            print('3. Qual tecnologia do dia a dia pode ser afetada por esse problema?')
            print('A) Geladeiras.')
            print('B) Satélites de GPS, internet e comunicação.')
            print('C) Bicicletas elétricas.')
            print('D) Impressoras.')
            resposta = input('Digite a letra da sua resposta: ').upper()
            while not validar(resposta):
                resposta = input('Digite uma resposta válida (A / B / C / D): ').upper()
                if validar(resposta):
                    break
            r_user.append(resposta)

            # Questão 4

            linha()
            print('4. O que acontece quando um satélite colide com outro objeto em órbita?')
            print('A) Produz milhares de fragmentos que podem causar novas colisões.')
            print('B) Ele desaparece sem deixar vestígios.')
            print('C) Cai imediatamente na Terra.')
            print('D) Fica invisível.')
            resposta = input('Digite a letra da sua resposta: ').upper()
            while not validar(resposta):
                resposta = input('Digite uma resposta válida (A / B / C / D): ').upper()
                if validar(resposta):
                    break
            r_user.append(resposta)

            # Questão 5

            linha()
            print('5. Se a Síndrome de Kessler atingir níveis críticos, qual pode ser a consequência?')
            print('A) As viagens espaciais se tornam mais seguras.')
            print('B) A Lua se afastará da Terra.')
            print('C) Os satélites ganharão mais vida útil.')
            print('D) O acesso ao espaço pode ficar extremamente difícil por séculos.')
            resposta = input('Digite a letra da sua resposta: ').upper()
            while not validar(resposta):
                resposta = input('Digite uma resposta válida (A / B / C / D): ').upper()
                if validar(resposta):
                    break
            r_user.append(resposta)

            # Finalização
            linha()
            print('FIM DO QUIZ!')
            voltar()

        case '4':
            if len(r_user) == 0:
                print('Você ainda não realizou o quiz. Volte quando estiver realizado!')
            else:
                n_r_c = 0  # Número Respostas Corretas - Quantidade de respostas corretas do usuário
                q_e = []   # Questões Erradas - Números que representam as questões erradas pelo usuário
                for i in range (len(r_gabarito)):      # Estrutura contadora de respostar corretas
                    if r_user[i] == r_gabarito[i]:
                        n_r_c += 1
                    else:
                        q_e.append(i+1)
                if n_r_c < 5:
                    print(f'Você acertou um total de {n_r_c} perguntas!')
                    if n_r_c <= 2:
                        print('Você ainda não conhece bem o problema. A Síndrome de Kessler pode comprometer tecnologias essenciais que usamos todos os dias.')
                    else:
                        print('Você entende os riscos principais. O aumento dos detritos espaciais é uma ameaça real para satélites e futuras missões espaciais.')
                    decisao = input('Deseja saber as questões que precisa acertar? S / N: ').upper()
                    while decisao != 'S' and decisao != 'N':   # Valida a decisão do usuário
                        print('Por favor, digite uma resposta válida. "S" para sim, "N" para não')
                        decisao = input('Deseja saber as questões que precisa acertar? S / N: ').upper()
                    if decisao == 'S':
                        print('Questões a acertar:')
                        for i in q_e:
                            print(f'Questão {i}')
                else:
                    print('PARABÉNS!!! Você acertou todas as respostas do Quiz!')
                    print('Você compreende a gravidade da Síndrome de Kessler e a necessidade de prevenção.')
            voltar()

        case '5':
            print('Programa encerrado, obrigado(a) por participar!')
            linha()
            break

        case _:
            print('Por favor, digite uma opção válida')
            print('Você deve digitar o número que represente sua escolha')