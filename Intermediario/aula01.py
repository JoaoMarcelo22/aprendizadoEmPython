# Estrutura de dados

# Listas

# Exemplos :

frutas = ['laranja', 'maca', 'uva',]
frutas = []
letras = list("python") 
numeros = list(range(10))
carro = ["ferrari", "F8", 42000, 2020, 2900, "Sao paulo", True]

# Acesso Direto

frutas[1] #maca
frutas[2] #uva
frutas[-1] #uva ultimo elemento
frutas[-3] #laranja 

# Listas aninhadas

matriz =[
    [1,"a",2],
    [3,"b",4],
    [5,"c",6]
]
matriz[0] #[1,"a",2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # 6

# Fatiamento

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::]   # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

# Literar listas
# Função enumerate

carros = ["gol", "celta", "palio"]

for indice,carro in carros:
    print(f'{indice}:{carro}')

# Compreensão de listas 
# filtros 

numeros = [1, 30, 21, 2, 9, 65, 34]
pares= [numero for numero in numeros if numero % 2 == 0] # versão 2
quadrado = [numero ** 2 for numero in numeros ] # Modificando valores V2

for numero in numeros:      # versão 1
    if numero % 2 == 0:
        pares.append(numero)

for numero in numeros:
    quadrado.append(numero ** 2) # Modificando valores V1