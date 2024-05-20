saldo, deposito, saque, transf = 5000,0,0,0
quantidade_saque = 3

def opcoes():
  print()
  print(f' ======= MENU =======')
  print()
  print('Selecione uma opção:')
  print('1 - Depositar')
  print('2 - Sacar')
  print('3 - Extrato')
  print('0 - Sair')
  print('======================')
  opcao = int(input())

  if opcao == 1:
    depositar(saldo)
  elif opcao == 2:
    sacar(saldo)
  elif opcao == 3:
    extrato(saldo)

def depositar(saldo):
    deposito = float(input('Defina o valor a depositar: '))
    saldo += deposito
    print(f'Seu saldo atual é de {saldo}')
    opcoes()

def sacar(saldo):
    saque = float(input('Defina o valor a sacar: '))
    if saque < 0:
        print('Valor inválido')
    elif saque <= 500:
        saldo -= saque
        print(f'Seu saldo atual é {saldo}')
    else:
        print('Valor excedido')
    opcoes()

def extrato(saldo):
    user = input('Para quem deseja transferir: ')
    transf = float(input('Defina o valor a transferir: '))
    if transf < 0:
        print('Valor de transferencia inválido')
    elif transf <= 2000:
        saldo -= transf
        print(f'R$ {transf} transferido para {user}')
    else:
        print('Valor de transferencia excedido')
    opcoes()

opcoes()
