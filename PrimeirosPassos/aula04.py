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

# O comando FOR é usado para percorrer um objeto iterável. Faz sentido usar For 
# quando sabemos o número exato de vezes que nosso bloco de codigo deve ser executado,
# ou quando queremos percorrer um objeto iterável (ex: palavra, cadeia de caracter)

texto =  input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executado no final do laço")

# RANGE é uma fucao built-in do python, ela e usada para produzir uma sequencia de numeros
# inteiros a partir de um inicio ( inclusivo ) para um fim ( exclusivo ). se usarmos rang(i,j)
# sera produzido : i, i+1, i+2, i+3, ..., j-1. [ não entendi foi nada ]
# recebe 3 argumenos: stop ( obrigatorio ), start ( opcional ) e step ( opcional )

list(range(4)) # Usando a base
# sainda : [0,1,2,3]

for numero in range(0,11): # usando o Start
    print(numero, end=" ")
# sainda : [0,1,2,3,4,5,6,7,8,9,10]

for numero in range(0, 51, 5): # Usando o Step
    print(numero, end=" ")
# sainda : tabuada de 5 ex [0,5,10...50]

# WHILE   é usado para repetir um bloco de codigo varias vezes. Faz sentido usar o while
# quando não sabemos o numero exato de vezes que nosso bloco de codigo deve ser executado.
opcao2 = -1

while opcao2 != 0:
    opcao2 = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao2 == 1:
        print("Sacando...")
    elif opcao2 == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema! ")

# Break corta e execução do programa

while True:
    numero2 = int(input("informe um numero :"))

    if numero2 == 2:
        break

    print(numero2)

for numero3 in range(100):
    if numero3 == 3:
        break

    print(numero3, end=" ")


# Continue contorna o numero ou seja ignora/pula
# presta atençao na ordem, se a logica do continue fazer pular a logica do break, a segunda logica nunca será usada.

for numero3 in range(100):
    if numero3 == 3:
        continue

    print(numero3, end=" ")