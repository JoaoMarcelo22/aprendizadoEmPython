# Operadores aritméticos

print( 1 + 1) # Adicao
print(10 - 2) # Subtracao
print(5 * 2)  # Multiplicacao
print(5 / 2)  # Divisao com casa flutuante
print(5 // 2) # Divisao com casa inteira
print(10 % 3) # Modulo
print(2 ** 3) # Exponenciacao

# Seguindo a ordem matematica 

# Operadores de comparacao

saldo = 450
saque = 200

print( saldo == saque) # Igual
print( saldo != saque) # Diferente
print( saldo > saque)  # Maior
print( saldo >= saque) # Maior ou igual
print( saldo < saque)  # Menor
print( saldo <= saque) # Menor ou igual

# Operadores de atribuicao

a = 10   # Atribuicao simples
a += 10  # Atribuicao com adicao
a -= 10  # Atribuicao com subtracao
a *= 10  # Atribuicao com multiplicacao
a /= 10  # Atribuicao com divisao simples
a //= 10 # Atribuicao com divisao com retorno inteiro

# Operadores logicos

limite = 100

saldo >= saque and saque <= limite  # And se refere ao operador E
saldo >= saque  or saque <= limite  # Or se refere ao operador Ou
not 1000 > 1500                     # Not se refere ao operador Negacao

# Operadores de identidate

curso = "Curso de python"
nome_curso = curso
valor1, valor2 = 200,200

curso is nome_curso         # Is compara se o objeto A(curso) e o objeto B(nome_curso) estão no mesmo local da memoria
curso is not nome_curso     # negacao ou seja false
valor1 is valor2            # compara ambos as variaveis e retorna true

# Operadores de associacao

curso = "Curso de Python"
frutas = ["laranja","uva", "limao"]
saques = [1500,100]

"Python" in curso       # In faz uma busca e retorna se encontrou True ou se não encontrou False
"maca" not in frutas    # Maca não esta presente, mas pelo operador not, o resultado é true
200 in saques           # retorna false já que 200 não está presente em saques