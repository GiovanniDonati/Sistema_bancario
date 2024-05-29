saldo = 0
valor = 0
limite = 500
extrato = ""
numero_saques = 0
QUANTIDADE_SAQUE = 3

menu = '''======== MENU ========

  Selecione uma opção:
    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair
======================\n\n'''

def deposito(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        print(f'Depósito de R$ {valor} efetuado com sucesso!\n')
        extrato +=  f'Depósito de R$ {valor:.2f}\n'
        print(saldo)
        
        return saldo, extrato

    else:
        print('Falha no depósito, valor inválido!')

#Usar as variaveis: saldo, valor, extrato, limite, numero_saque, limite_saques
def sacar(saldo, valor, extrato):
    if valor > saldo:
        print('Saldo insuficiente!')

    elif valor > limite:
        print('Valor do saque superior ao limite!')

    elif numero_saques >= QUANTIDADE_SAQUE:
        print('Excedido o número de saques diários')

    elif valor > 0:
        valor = float(input("Digite o valor do saque:"))
        saldo -= valor
        print(f'Saque de R$ {valor} efetuado com sucesso!')
        extrato +=  f'Saque de R$ {valor}'

    else:
        print('Valor inválido!')

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor do depósito: "))

        deposito(saldo=saldo, valor=valor, extrato=extrato)

    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))

        sacar(saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                QUANTIDADE_SAQUE = QUANTIDADE_SAQUE)

    elif opcao == 3:
        print('\n======== EXTRATO ========')
        print('Não forma realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('========================\n')

    elif opcao == 0:
        print('''Obrigado por usar nosso sistema bancário!
              Volte Sempre!''')
        exit
        
    else:
        print('Operação inválida, tente novamente!')
