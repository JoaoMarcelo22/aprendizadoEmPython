# Funcoes

# Parametros especiais
# posição, nome posição, nome

# Positional Only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # antes da barra é obrigado a passar por posição
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio", 1999, "ABC-123", marca="fiat", motor="1.0",combustivel="gasolina") # Válido

criar_carro(modelo="palio", ano=1998, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina") # Inválido

# Keyword only

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel): # como o * todos deve ser passados por nome e valor
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="palio", ano=1998, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="gasolina") # Válido

criar_carro2("palio", 1998, "ABC-123", marca="Fiat", motor="1.0", combustivel="gasolina") #Inválido

# Keyword and positional only

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel): # como o * todos deve ser passados por nome e valor
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3(modelo="palio", ano=1998, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="gasolina") # inválido

criar_carro3("palio", 1998, "ABC-123", marca="Fiat", motor="1.0", combustivel="gasolina") # Válido

# Objetos de primera classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a,b,funcao):
    resultado =  funcao(a, b)
    if funcao == somar:
        operador = " + "
    elif funcao == subtrair:
        operador = " - "
    print(f"O resultado da operação {a} {operador} {b} = {resultado}")

exibir_resultado(10,10,somar)

# Escopo local e escopo global

salario = 200

def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    
    salario += bonus
    return salario

lista= [1]
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)
print(lista)