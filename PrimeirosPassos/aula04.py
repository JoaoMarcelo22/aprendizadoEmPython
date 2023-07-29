# Estruturas condicionais e de repeticao

# Identacao e blocos
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print("retire o dinheiro")
    
    print("obrigado por seu nosso cliente")

sacar(1000)

# Estruturas condicionais 

opcao = int(input("Informe uma opcao: [1] Sacar \n [2] Extrato:"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato ... ")
else:
    print("Opcao invalida")

# If = SE , elif = SenaoSe, else = Senao

# Estrutura condicional ternaria

saldo = 200
saque = 150

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

# Estrutura de repeticao
