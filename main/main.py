import textwrap

def menu():
    menu = '''\n
    ======== MENU ========

    Selecione uma opção:
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Nova conta
        5 - Exibir contas
        6 - Novo Usuário 
        0 - Sair
    ======================\n\n'''

    return input(textwrap.dedent(menu))
    
def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato +=  f'Depósito de R$ {valor:.2f}\n'
        print(f'Depósito de R$ {valor} efetuado com sucesso!\n')
    else:
        print('Falha no depósito, valor inválido!')
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, QUANTIDADE_SAQUE):
    if valor > saldo:
        print('Saldo insuficiente!')

    elif valor > limite:
        print('Valor do saque superior ao limite!')

    elif numero_saques >= QUANTIDADE_SAQUE:
        print('Excedido o número de saques diários')

    elif valor > 0:
        saldo -= valor
        extrato +=  f'Saque de R$ {valor}'
        numero_saques += 1
        print(f'Saque de R$ {valor} efetuado com sucesso!')

    else:
        print('Valor inválido!')

    return saldo, extrato

def extrato_conta(saldo, /, *, extrato):
        print('\n======== EXTRATO ========')
        print('Não forma realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('========================\n')

def criar_usuario(usuarios):
    cpf = input("Infome o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existentecom esse CPF!")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, Número - Bairro - Cidade/Sigla Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, criação de conta encerrada! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    QUANTIDADE_SAQUE = 3
    AGENCIA = '0001' 

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        opcao = int(opcao)

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor,extrato)

        elif opcao == 2:
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                QUANTIDADE_SAQUE = QUANTIDADE_SAQUE)

        elif opcao == 3:
            extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            print('''Obrigado por usar nosso sistema bancário!
                Volte Sempre!''')
            break
            
        else:
            print('Operação inválida, tente novamente!')

main()