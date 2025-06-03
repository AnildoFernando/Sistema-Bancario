import os

def linha():
    print(24 * '=')

def limpar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')

#Saldo da conta, extrato e contador para definir limite dos saques
saldo = 0
lista_extrato = []
contador_saque = 0

while True:
    #Valor do deposito e saque temporário
    deposito = 0
    saque = 0

    operacoes = int(input('''========= MENU =========
      [1]DEPÓSITO
      [2]SAQUE
      [3]EXTRATO
      [0]ENCERRAR
========================
Digite sua opção: '''))
    linha()

    if operacoes == 1:
        deposito = float(input('Digite o valor do depósito:\nR$ '))
        linha()
        #depositar somente valores positivos
        if deposito > 0:
            saldo += deposito
            mensagem = (f'Depósito de R${deposito:.2f} com sucesso.')
            lista_extrato.append(mensagem)
            limpar_terminal()
            print(mensagem)
            linha()
        else:
            mensagem = (f'Saque de R${deposito:.2f} é um valor inválido. ')
            lista_extrato.append(mensagem)
            limpar_terminal()
            print(mensagem)
            linha()
            
    if operacoes == 2:
        #somente 3 saques diários de até R$500 cada, caso não haja saldo, exiba uma mensagem
        if contador_saque == 3:
            limpar_terminal()
            print (f'Limite de saques diários atingidos. Tente novamente amanhã.')
            linha()
        if contador_saque < 3:
            saque = float(input('Digite o valor do saque:\nR$ '))
            linha()
            if saque < 500.00:
                if saque <= saldo:
                    saldo -= saque
                    mensagem = (f'Saque de R${saque:.2f} com sucesso')
                    contador_saque += 1
                    lista_extrato.append(mensagem)
                    limpar_terminal()
                    print(mensagem)
                    linha()
                else:
                    mensagem(f'Saque de R${saque:.2f} indisponivel. Saldo insuficiente.')
                    lista_extrato.append(mensagem)
                    limpar_terminal()
                    print(mensagem)
                    linha()
            else:
                mensagem = (f'Saque de R${saque:.2f} não permitido, limite de R$500.00.')
                lista_extrato.append(mensagem)
                limpar_terminal()
                print(mensagem)
                linha()
    
    if operacoes == 3:
        limpar_terminal()
        linha()
        print(f'R${saldo:.2f} - Valor total de saldo.')
        linha()
        if lista_extrato == []:
            print('Não foram feitas movimentações.')
        for item in lista_extrato:
            print(item)
        linha()
        voltar = int(input('Digite [0] para retornar: '))
        limpar_terminal()

    if operacoes == 0:
        print('Encerrando, tenha um bom dia!')
        break
