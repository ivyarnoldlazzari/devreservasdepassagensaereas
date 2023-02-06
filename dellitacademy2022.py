import random

# Dicionário para o avião
aviao_base = {"D": list(range(1, 201)), "C": [], "R": [], "valor": 0}

# Dicionário para alocar informações dos vôos
aviao = {}

# Dicionário para alocar informações das compras
informacoes_id = {}

poltrona = {}
poltronas_janela_direita = {50}
poltronas_corredor_direita = {50}
poltronas_janela_esquerda = {50}
poltronas_corredor_esquerda = {50}

# Menu
print("***************************************************************")
print("*********|BEM-VINDO AO MENU DA EMPRESA AÉREA PYTHON|***********")
print("***************************************************************")
print('+-------------------------------------------------------------+')
print('| OPÇÃO                      ||            CÓDIGO             |')
print('+-------------------------------------------------------------+')
print('| MAPA DE ASSENTOS           ||               1               |')
print('+-------------------------------------------------------------+')
print('| COMPRAR/RESERVAR/CANCELAR  ||               2               |')
print('+-------------------------------------------------------------+')
print('| INFORMAÇÕES DA PASSAGEM    ||               3               |')
print('+-------------------------------------------------------------+')
print('| SAIR DO PROGRAMA           ||               4               |')
print('+-------------------------------------------------------------+')

opcoesCodigo = ['1', '2', '3', '4']  # Lista de códigos

codigo = int(input('\nDigite o código correspondente a opção desejada: '))
print('\n')


if(codigo == 1):
        print("***************************************************************")
        print("              | BEM-VINDO AO MAPA DE ASSENTOS|                 ")
        print("***************************************************************")



        for poltrona in poltronas_janela_direita:
                print('[{}] '.format(poltrona if poltrona else ' '), end='')
        print(' \\  : 50 assentos nas Janelas Direitas')

        print('  |   |  ', end='')
        for poltrona in poltronas_corredor_direita:
                print('[{}]'.format(poltrona if poltrona else ' '), end='')
        print('  | : 50 assentos no Corredor da Direita')

        print('  | __|_ ', end='')
        for poltrona in poltronas_corredor_esquerda:
                print('[{}]'.format(poltrona if poltrona else ' '), end='')
        print('  | : 50 assentos no Corredor da Esquerda')

        print('   \\     ', end='')
        for poltrona in poltronas_janela_esquerda:
                print('[{}]'.format(poltrona if poltrona else ' '), end='')
        print(' /  : 50 assentos nas Janelas Esquerdas')






elif(codigo == 2):
        # Segundo menu
        print("***************************************************************")
        print("     | BEM-VINDO AO MENU DE COMPRAS/RESERVAS/CANCELAMENTO     |")
        print("***************************************************************")
        print('+-------------------------------------------------------------+')
        print('| OPÇÃO                      ||            CÓDIGO             |')
        print('+-------------------------------------------------------------+')
        print('| COMPRAS                    ||               1               |')
        print('+-------------------------------------------------------------+')
        print('| RESERVAS                   ||               2               |')
        print('+-------------------------------------------------------------+')
        print('| CANCELAMENTO               ||               3               |')
        print('+-------------------------------------------------------------+')
        print('| SAÍDA                      ||               4               |')
        print('+-------------------------------------------------------------+')

        opcoesCodigo2 = ['1', '2', '3', '4']  # Lista de códigos

        codigo2 = int(input("Escolha a próxima ação: "))
        if(codigo2 == 1):
                print("***************************************************************")
                print("               | BEM-VINDO AO SETOR DE COMPRAS |               ")
                print("***************************************************************")

                destino = input('\nQual o seu destino? ')
                print('Seu destino é {}. Vamos buscar as melhores oportunidades para você!'.format(destino.title()))

                if destino.lower() in list(aviao.keys()):  # Verificação de Destino no dicionário do avião
                        local = destino.lower()

                else:
                        valor_Voo = random.randint(800,2000)  # Gerando valor do vôo aleatóriamente entre os valores 800 e 2000
                        aviao[destino.lower()] = aviao_base
                        aviao[destino.lower()]['valor'] = valor_Voo
                        local = destino.lower()

                print(f'\nO voo possui {len(aviao[local]["D"])} assentos, {len(aviao[local]["D"]):.0f} disponíveis, '
                      f'{len(aviao[local]["C"]):.0f} comprados e {len(aviao[local]["R"])} reservados. '
                      f'\nO valor do vôo é ' f'{aviao[local]["valor"]} reais.')

                escolha = input('Deseja Comprar? ')


                if (escolha == 'sim' or escolha == 'Sim'):
                        passagens = int(input(f'Quantas passagens você deseja comprar? '))
                        print("Parabéns! Você comprou ", passagens, "passagem/passagens.") # Mostra quantas passagens foram compradas



        elif(codigo2 == 2):
                print("***************************************************************")
                print("               | BEM-VINDO AO SETOR DE RESERVAS |              ")
                print("***************************************************************")

                reserva = int(input('Quantas passagens você deseja reservar? '))
                print("Você reservou ", reserva, "passagem/passagens.")  # Mostra quantas passagens foram reservadas




        elif(codigo2 == 3):
                print("***************************************************************")
                print("              | BEM-VINDO AO SETOR DE CANCELAMENTO |           ")
                print("***************************************************************")

                print("Digite compras ou então reservas, para escolher o que você deseja cancelar.")
                cancelamento_compras_ou_vendas = input('Digite aqui: ')
                if(cancelamento_compras_ou_vendas == 'Compras' or cancelamento_compras_ou_vendas == 'compras' ):
                        print("Você quer cancelar a compra")

                elif(cancelamento_compras_ou_vendas == 'Reservas' or cancelamento_compras_ou_vendas == 'reservas'):
                        print("Você quer cancelar a reserva")

                else:
                        print("Você digitou algo errado.")


                cancelamento = int(input('Quantas passagens você deseja cancelar? '))
                print("Você cancelou ",cancelamento, "passagem/passagens.")  # Mostra quantas passagens foram canceladas

        else:
                print("Saindo do menu compras/reservas/cancelamento")




elif(codigo == 3):
        print("***************************************************************")
        print("               | BEM-VINDO AO RESUMO DA PASSAGEM |             ")
        print("***************************************************************")

        print('Vamos conferir as informações da sua passagem!')
        codigo_do_cliente = int(input("Digite o código do cliente: "))

        print("Código do Cliente: ",codigo_do_cliente)
        print("Assentos comprados:  ")
        print("Assentos reservados: ")
        print("Assentos cancelados: ")
        print("Valor final:         ")



elif(codigo == 4):
        print("Volte sempre!")

else:
        print("Você digitou uma opção errada!")

