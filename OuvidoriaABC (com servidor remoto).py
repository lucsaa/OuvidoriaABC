import mysql.connector

connection = mysql.connector.connect(
    host='remotemysql.com',
    user='KDVYXP7CIN',
    password='JkjkPqMjEd',
    database='KDVYXP7CIN'
)

cursor = connection.cursor()

sql = "SELECT * FROM manifestacoes"

cursor.execute(sql)
manifestacoeslista = cursor.fetchall()

cursor.close()

opcao = -9

while opcao != 7:
    print(''' Centro universitário ABC
    Sistema de OUVIDORIA

    Opções  de interação:
    1) Abrir todas as manifestações feitas;
    2) Abrir todas as sugestões feitas;
    3) Abrir todas as reclamações feitas;
    4) Abrir todos os elogios feitos;
    5) Criar e adicionar manifestação;
    6) Pesquisar manifestação pelo número do protocolo;
    7) Sair do sistema.''')
    print()

    cursor = connection.cursor()

    opcao = int(input(
        'Baseado no que está sendo apresentado acima, digite o número correspondente para ter acesso no sistema: '))
    print()
    if opcao == 1:
        print(5 * '=', ' Todas as manifestações feitas no sistema ', 5 * '-=-')
        sql="SELECT * FROM manifestacoes"

        cursor.execute(sql)
        manifestacoesdb=cursor.fetchall()

        cursor.close()

        for manifestacao in manifestacoesdb:
            print('Código:',manifestacao[0],'- Nome:',manifestacao[1],'- Tipo:',manifestacao[2],'- Descrição:',manifestacao[3])
        print()
    elif opcao == 2:
        sql="SELECT * FROM manifestacoes WHERE tipo='Sugestão'"

        cursor.execute(sql)
        manifestacoesdb=cursor.fetchall()

        cursor.close()

        for manifestacao in manifestacoesdb:
            print('Código:',manifestacao[0],'- Nome:',manifestacao[1],'- Descrição:',manifestacao[3])
        print()
    elif opcao == 3:
        sql="SELECT * FROM manifestacoes WHERE tipo='Reclamação'"

        cursor.execute(sql)
        manifestacoes=cursor.fetchall()

        cursor.close()

        for manifestacao in manifestacoes:
            print('Código:',manifestacao[0],'- Nome:',manifestacao[1],'- Descrição:',manifestacao[3])
        print()
    elif opcao == 4:
        sql="SELECT * FROM manifestacoes WHERE tipo='Elogio'"

        cursor.execute(sql)
        manifestacoesdb=cursor.fetchall()

        cursor.close()

        for manifestacao in manifestacoesdb:
            print('Código:',manifestacao[0],'- Nome:',manifestacao[1],'- Descrição:',manifestacao[3])
        print()
    elif opcao == 5:
        print(5 * '=', ' Preencha os dados para criar uma nova manifestação ', 5 * '=')
        print()
        protocolo = len(manifestacoeslista) + 1
        nome = str(input('Digite o nome que irá aparecer na manifestação: '))
        print()
        tipo = -1
        while tipo < 1 or tipo > 3:
            tipo = int(
                input('Digite um número correspondente ao tipo escolhido. 1) Sugestão; 2) Reclamação; 3) Elogio: '))
            if tipo < 1 or tipo > 3:
                print('O dado {} informado é inválido. Tente novamente.'.format(tipo))
        if tipo==1:
            tipo="Sugestão"
        if tipo==2:
            tipo="Reclamação"
        if tipo==3:
            tipo="Elogio"
        print()
        descricao = str(input('Descreva a sua manifestação: '))

        sql = 'INSERT INTO manifestacoes (protocolo, nome, tipo, relato) VALUES(%s, %s, %s, %s)'
        data=(protocolo,nome,tipo,descricao)

        novaManifestacao=(str(protocolo)+nome+tipo+descricao)
        manifestacoeslista.append(novaManifestacao)

        cursor.execute(sql,data)
        connection.commit()

        userid=cursor.lastrowid

        cursor.close()

        print()
    elif opcao == 6:
        search = -1
        numeroManifestacoes = len(manifestacoeslista)
        while search < 1 or search > numeroManifestacoes:
            search = int(input('Digite o número do protocolo da manifestação que você deseja ver: '))
            if search < 1 or search > numeroManifestacoes:
                print('Não existe manifestação com este número de protocolo.')
            else:
                sql='SELECT * FROM manifestacoes where protocolo ='+str(search)

                cursor.execute(sql)
                manifestacoesdb=cursor.fetchall()

                cursor.close()

                for manifestacao in manifestacoesdb:
                    print('Nome:',manifestacao[1],'- Tipo:',manifestacao[2],'- Descrição:',manifestacao[3])

        print()
    elif opcao == 7:
        print('Saindo do sistema ...')
    else:
        print('O dado {} informado é inválido'.format(opcao))

connection.close()