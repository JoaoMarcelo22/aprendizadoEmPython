# Tupla

# Tupla são imutaveis

frutas = ( "laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)

frutas[0]
frutas[2]

matriz =[
    (1,"a",2),
    (3,"b",4),
    (5,"c",6)
]
matriz[0] #[1,"a",2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # 6

# Fatiamento

tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:] # ["t", "h", "o", "n"]
tupla[:2] # ["p", "y"]
tupla[1:3] # ["y", "t"]
tupla[0:3:2] # ["p", "t"]
tupla[::]   # ["p", "y", "t", "h", "o", "n"]
tupla[::-1] # ["n", "o", "h", "t", "y", "p"]

# Metodos disponiveis

tupla.count()
tupla.index()
len(tupla)