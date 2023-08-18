# Conjunto

set([1,2,3,1,3,4]) # 1,2,3,4 retira a duplicação
set("abacaxi") # a, b, c, x, i Não traz em ordem
set(("palio", "gol", "celta", "palio")) # gol, celta, palio

linguagens = { "python", "java", "python"} # declaração ao set
print(linguagens)

# Acessando dados

numeros = {1,2,3,2}
numeros = list(numeros)

print(numeros[0])

# Enumarate

carros = {"gol", "celta", "palio" }

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

# Funcoes matematicos 

# Union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # { 1, 2, 3, 4 } faz a junção de dois conjuntos

# Intersection

conjunto_c = { 1, 2, 3}
conjunto_d = { 2, 3, 4}


conjunto_c.intersection(conjunto_d) # {2, 3} retorna os valores em comum

# difference

conjunto_e = { 1, 2, 3}
conjunto_f = { 2, 3, 4}

conjunto_e.difference(conjunto_f) # {1} retorna os valores diferentes
conjunto_f.difference(conjunto_e) # {4} retorna os valores diferentes

# Symmetric_difference

conjunto_g = { 1, 2, 3}
conjunto_h = { 2, 3, 4}

conjunto_g.symmetric_difference(conjunto_h) # {1, 4} retorna os valores diferente em cada conjunto, JUNTOS

# Issubset / issuperset

conjunto_i = { 1, 2, 3}
conjunto_j = { 4, 1, 2, 5, 6, 3}
conjunto_k = { 7, 8, 9}

conjunto_i.issubset(conjunto_j) # TRUE ou seja o conjunto I esta presente no J.
conjunto_j.issubset(conjunto_i) # False ou seja o conjunto J não esta presente no I por inteiro.

conjunto_i.issuperset(conjunto_j) # é o inverso do anterior
conjunto_j.issuperset(conjunto_i) 

conjunto_i.isdisjoint(conjunto_j) # False existem numero em comum
conjunto_i.isdisjoint(conjunto_k) # True, nenhum numero são semelhantes
conjunto_k.add(69) # adiciona, caso o numero exista ele não será encrimentado
conjunto_k.clear()
conjunto_k.copy()
conjunto_k.discard(69) # discarta um valor
conjunto_k.pop()
conjunto_k.remove(69) # Caso o elemento não exista ele da erro
len(conjunto_k)

# IN

numeroes = {1,2,3,4,5,6}
1 in numeros # true
10 in numeros # false
