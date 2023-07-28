## Tipos de Dados em Python e Variaveis / Constantes

age = 25 ## inteiro
name = "jubileu" ## string
dollar = 3.2 ## float
relly = True ## boolean
lists = [ ## list
    'SP',
    'RJ',
    'MG',
]
print(f'My name is {name}, i am {age} year old. i need {dollar} dollares. You from {lists} right {relly} ??')

## Não existe constante em Python, apenas usamos uma convenção usando string maiusculas.

DEBUG = True
AMOUNT = 30.2

## Use o padrão em snake case

year_old = 25

## Conversão de tipos

palavra = '10'
inteiro = 10
flutuante = 10.0

palavra = float(palavra) # convertendo para Float
print(palavra)
palavra = int(palavra) # convertendo para inteiro
print(palavra)
palavra = str(palavra) # convertendo para string
print(type(palavra))

# Podemos dividir e ter um valor inteiro no resultado usando //
# input e output

nome = input("Informe o seu nome: ")

sobrenome = input("Informe o seu sobrenome: ")

# há 4 atributos opcionais para o print
print(nome, sobrenome) # ex: jaum silva
print(nome, sobrenome, end="...\n") # ex: jaum silva...
print(nome, sobrenome, sep="#") # ex: jaum#silva
