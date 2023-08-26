import textwrap


def menu():
    menu = """\n
    ============= MENU ============
    [1]\tSacar
    [2]\tDepositar
    [3]\tExtrato
    [4]\tSair
    [5]\tCriar usuario
    [6]\tCriar conta
    [7]\tListar contas
    ------------------------  
    Informe uma opcao:
    ------------------------\n  
    """
    return int(input(textwrap.dedent(menu)))

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(" O valor excede o limite.")
    elif excedeu_saques:
        print(" Numero de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque = R$: {valor:.2f}\n'
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("Valor invalido, informe um numero inteiro e positivo")
    return saldo, extrato
     
def deposito(saldo, valor, extrato, /):

    if valor <= 0:
        print("Valor incoeso, informe um numero positivo valido.")

    else:
        saldo += valor
        extrato += f'Deposito = R$: {valor:.2f}\n'
        print("Deposito realizado com sucesso!")

        return saldo, extrato
        
def exibir_extrato(saldo,/,*, extrato):

    print("\n ============== Extrato ================")
    print("\n Não há movimentações." if not extrato else extrato)
    print(f"\n Saldo :\t\tR$: {saldo:.2f}")
    print(" ======================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF ( Somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Já existe usuario com esse CPF:")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nº - bairro - cidade/estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print(" Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [ usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("\n Usuario não encontrado")

def listar_contas(contas):
      for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}  
        """
        print("="* 40) 
        print(textwrap.dedent(linha))

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:
        opcao = menu()

        if opcao == 1 :

            valor = float(input("Informe o valor do saque :"))
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES)

        elif opcao == 2:
            valor = float(input("Informe o valor do deposito :"))
            saldo,extrato = deposito(saldo, valor, extrato)

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            break

        elif opcao == 5:
            criar_usuario(usuarios)

        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 7:
            listar_contas(contas)

        else:
            print("Opção inaquado, informe uma opção correta\n")

main()