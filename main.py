import os

# Função para imprimir linha de separação
def linha():
    print(32 * '=')

# Função para limpar o terminal
def limpar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:
        os.system('clear')

# Função para exibir o menu
def menu():
    escolha = input('''========= MENU =========
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] NOVO USUÁRIO
    [5] NOVA CONTA
    [6] LISTAR CONTAS
    [0] ENCERRAR
========================
Digite sua opção: ''')
    linha()
    return escolha

# Função para realizar saques
def saque(*, saldo, extrato_total, valor_limite, numero_saque, limite_saque):
    if numero_saque == limite_saque:
        limpar_terminal()
        print('Limite de saques diários atingido. Tente novamente amanhã.')
        linha()
        return saldo, extrato_total, numero_saque

    while True:
        try:
            valor = float(input('Digite o valor do saque:\nR$ '))
            linha()
            if valor <= 0:
                print('O valor do saque deve ser maior que zero.')
                continue
            if valor > valor_limite:
                print(f'O valor máximo permitido por saque é R${valor_limite:.2f}.')
                continue
            if valor <= saldo:
                saldo -= valor
                numero_saque += 1
                mensagem = f'Saque de R${valor:.2f} realizado com sucesso.'
                extrato_total.append(mensagem)
                limpar_terminal()
                print(mensagem)
                linha()
                return saldo, extrato_total, numero_saque
            else:
                print('Saldo insuficiente para este saque.')
        except ValueError:
            print('Entrada inválida. Digite apenas números.')

# Função para realizar depósitos
def deposito(saldo, extrato_total, /):
    while True:
        try:
            valor = float(input('Digite o valor do depósito:\nR$ '))
            linha()
            if valor > 0:
                saldo += valor
                mensagem = f'Depósito de R${valor:.2f} com sucesso.'
                extrato_total.append(mensagem)
                limpar_terminal()
                print(mensagem)
                linha()
                return saldo, extrato_total
            else:
                print('Valor inválido. O depósito deve ser maior que zero.')
        except ValueError:
            print('Entrada inválida. Digite apenas números.')

# Função para exibir o extrato da conta
def extrato(saldo, /, *, extrato_total):
    limpar_terminal()
    print(24 * '=')
    print(f'R${saldo:.2f} - Valor total de saldo.')
    print(24 * '=')
    if not extrato_total:
        print('Não foram feitas movimentações.')
    else:
        for linha_extrato in extrato_total:
            print(linha_extrato)
    print(24 * '=')
    while True:
        voltar = input('Digite [0] para retornar: ')
        if voltar == "0":
            limpar_terminal()
            return

# Função para criar um novo usuário
def criar_usuario(usuarios):
    limpar_terminal()
    print('============ ÁREA DE CADASTRO ============')
    cpf = input('Digite seu CPF sem pontos (.) ou traços (-): ').strip()
    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido. Deve conter apenas 11 números.')
        return

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('CPF já cadastrado. Não é possível criar um novo usuário com o mesmo CPF.')
        return

    nome = input('Digite seu nome completo: ').strip()
    data_de_nascimento = input('Digite sua data de nascimento (DD-MM-AAAA): ').strip()
    endereco = input('Digite seu endereço como no exemplo abaixo:\nLogradouro, número - bairro - cidade / sigla do estado\n= ').strip()

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_de_nascimento': data_de_nascimento,
        'endereco': endereco
    })

    print('Usuário cadastrado com sucesso!')

# Função para filtrar usuário por CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar uma nova conta
def nova_conta(agencia, numero_da_conta, usuarios, contas):
    cpf = input('Digite seu CPF sem pontos (.) ou traços (-): ').strip()
    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido. Deve conter apenas 11 números.')
        return

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        numero_da_conta = max([conta['numero_da_conta'] for conta in contas], default=0) + 1
        print('Conta criada com sucesso!')
        return {
            'agencia': agencia,
            'numero_da_conta': numero_da_conta,
            "usuario": usuario
        }
    else:
        limpar_terminal()
        print('Erro ao criar a conta. Cadastre um novo usuário primeiro.')

# Função para listar todas as contas cadastradas
def listar_contas(contas):
    limpar_terminal()
    print(30 * '=')
    print('===== CONTAS CADASTRADAS =====')
    print(30 * '=')
    if not contas:
        print('Nenhuma conta cadastrada.')
    else:
        for conta in contas:
            print(f'''Agência: {conta['agencia']}
C/C: {conta['numero_da_conta']}
Titular: {conta['usuario']['nome']}
            ''')
    print(30 * '=')
    while True:
        voltar = input('Digite [0] para retornar: ')
        if voltar == "0":
            limpar_terminal()
            return

# Função principal do programa
def main():
    agencia = "0001"
    contas = []
    numero_da_conta = 0
    usuarios = []
    saldo = 0
    extrato_total = []
    numero_saque = 0
    limite_saque = 3
    valor_limite = 500

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato_total = deposito(saldo, extrato_total)

        elif opcao == "2":
            saldo, extrato_total, numero_saque = saque(
                saldo=saldo,
                extrato_total=extrato_total,
                valor_limite=valor_limite,
                numero_saque=numero_saque,
                limite_saque=limite_saque
            )

        elif opcao == "3":
            extrato(saldo, extrato_total=extrato_total)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = nova_conta(agencia, numero_da_conta, usuarios, contas)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            limpar_terminal()

# Executa o programa
main()
