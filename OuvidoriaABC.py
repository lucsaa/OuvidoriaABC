opcao = 2
manifestacoes = []
sugestoes = []
reclamacoes = []
elogios = []

while opcao != 7:
    print()
    print('OUVIDORIA ABC')
    print('1) Listar todas as manifestações')
    print('2) Listar todas as sugestões')
    print('3) Listar todas as reclamações')
    print('4) Listar todos os elogios')
    print('5) Enviar uma manifestação (criar uma nova)')
    print('6) Pesquisar protocolo por número (ID)')
    print('7) Sair')
    print()
    opcao = int(input('Digite a opção: '))
    print()
    n = 0

    if opcao == 1:
        print('Lista de manifestações')
        for m in range(len(manifestacoes)):
            mQuebrado = (manifestacoes[n].split('#'))
            print('Código', mQuebrado[0], '- Tipo', mQuebrado[2], '– Requisitante', mQuebrado[1], '– ', mQuebrado[3])
            n = n + 1
    elif opcao == 2:
        print('Lista de sugestões')
        for m in range(len(sugestoes)):
            mQuebrado = (sugestoes[n].split('#'))
            print('Código', mQuebrado[0], '– Requisitante', mQuebrado[1], '– ', mQuebrado[3])
            n = n + 1

    elif opcao == 3:
        print('Lista de reclamações')
        for m in range(len(reclamacoes)):
            mQuebrado = (reclamacoes[n].split('#'))
            print('Código', mQuebrado[0], '– Requisitante', mQuebrado[1], '– ', mQuebrado[3])
            n = n + 1

    elif opcao == 4:
        print('Lista de elogios')
        for m in range(len(elogios)):
            mQuebrado = (elogios[n].split('#'))
            print('Código', mQuebrado[0], '– Requisitante', mQuebrado[1], '– ', mQuebrado[3])
            n = n + 1

    elif opcao == 5:
        requisitante = (input('Digite o nome do requisitante: '))
        tipo = (input('Digite o tipo (1 para reclamação, 2 para sugestão e 3 para elogio): '))
        descricao = (input('Digite a descrição: '))
        print()
        print('Manifestação adicionada com sucesso')

        if tipo == '1':
            tiponome = 'Reclamação'
        elif tipo == '2':
            tiponome = 'Sugestão'
        elif tipo == '3':
            tiponome = 'Elogio'
        codigo = str(len(manifestacoes) + 1)

        manifestacao = (codigo + '#' + requisitante + '#' + tiponome + '#' + descricao)

        manifestacoes.append(manifestacao)
        if tipo == '1':
            reclamacoes.append(manifestacao)
        elif tipo == '2':
            sugestoes.append(manifestacao)
        elif tipo == '3':
            elogios.append(manifestacao)
    elif opcao == 6:
        protocolo = int(input('Digite o número do protocolo: '))
        mQuebrado = (manifestacoes[protocolo - 1].split('#'))
        print(mQuebrado[0])
        print(mQuebrado[1])
        print(mQuebrado[2])
        print(mQuebrado[3])
    elif opcao > 7 or opcao <= 0:
        print('Entrada inválida')
