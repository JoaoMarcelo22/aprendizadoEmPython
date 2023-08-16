# Manipulando string

# Metodos

curso = "pYtHon"
curso2 = "  Python "
curso3 = "Python"

print(curso.upper()) # Maiusculo
print(curso.lower()) # Minusculo 
print(curso.title()) # Titulo
print(curso2.strip()) # Remove os espaços da direita e esquerda
print(curso2.lstrip()) # Remove apenas os espaços da esquerda 
print(curso2.rstrip()) # Remove os espaços apenas da direita
print(curso3.center(10,"#")) # Cria uma nova string e adiciona um caracter no inicio e fim
print(".".join(curso3)) # Cria um nova string separado por um caractere

# Interpolação

nome = "jurandi"
idade = 28
profissao = "dev"
linguagem = "python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome,idade,profissao,linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de pi : {PI:.2f}")
print(f"Valor de pi : {PI:10.2f}")

# Fatiamento 

nome2 = "jurandi costa albino"

nome2[0] # Retorna o primeiro caracter apenas "j"
nome2[:7] # Retorna do primeiro elemento até o 6º "jurandi"
nome2[8:] # Retorna a partir do 9 "costa albino"
nome2[8:13] # Retorna entre X e Y "costa"
nome2[8:13:2] # retorna de 2 em d2
nome2[:] # Retorna tudo
nome2[::-1] # Retorna o espelo "invertido"

# String Multiplas linhas

nome3 = "jurandi"
mensagem = f'''
    Olá meu nome é {nome3}
    Eu estou aprendendo Python.
    Essa mensagem tem diferentes recursos.
'''
print(mensagem)