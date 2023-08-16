menu = """

    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair
------------------------  
Informe uma opcao:
------------------------  
"""
valor_conta = 0
opcao = -1
saques = 0
extrato = ""

while opcao != 0:
    opcao = int(input(menu))

    if opcao == 1:
        if saques >= 3:
            print('Você já atigiu o limites de saques diarios.\n')
        else:
            valor = float(input("Informe a quantia para o saque de até R$:500,00 : "))
            if valor < 0 or valor > 500:
                print('Adicione um valor maior que 0 e inferior a 500\n')
            elif valor > valor_conta: 
              print('Valor superior ao valor existente em conta.\n')
            else:
                valor_conta -= valor
                saques += 1
                extrato += f'Saque: R$: {valor:.2f}\n'

    elif opcao == 2:
        valor = float(input("Informe a quantia para o depósito: "))
        if valor < 0:
            print('Valor invalido, Digite um valor positivo valido.\n')
        else :
            valor_conta += valor
            print(f'Valor de {valor:.2f} depositado com sucesso.\n')
            extrato += f'Deposito: R$: {valor:.2f}\n'

    elif opcao == 3:
        print("\n------------------ Extrato -------------------")
        print(extrato)
        print(f'Você tem {valor_conta:.2f} reais em sua conta\n')

    elif opcao == 4:
        print("Obrigado por usar nosso sistema!\n")
        break
    else:
        print(f'Opcao invalida\n')