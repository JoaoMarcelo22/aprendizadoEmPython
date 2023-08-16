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