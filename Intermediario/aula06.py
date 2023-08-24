# Funcoes

def exibir_mensagem():
    print("Hello Word!")

def exibir_mensagem2(nome):     # obrigado a passar o argumento
    print(f"Olá {nome}!")

def exibir_mensagem3(nome= "jose"):  # nopcional a passagem de argumento
    print(f"Olá {nome}!")

exibir_mensagem()
exibir_mensagem2(nome="joao")
exibir_mensagem3()
exibir_mensagem3(nome="Julius")

# Exemplo via Return

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("hello mundo")

print(func_3())
calcular_total([10, 20, 34])
retorna_antecessor_e_sucessor(10)

# Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa ):
    print(f"carro inserido com sucesso !{marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat","palio",1999,"ABC-1234")
salvar_carro(marca="fiat",modelo="palio",ano=1999,placa="ABC-1234")
salvar_carro(**{"marca":"fiat","modelo":"palio","ano":1999,"placa":"ABC-1234"})

# Args e Kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}"for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", " Beautiful is better than ugly.", autor= "Tim Peters", ano=1999)