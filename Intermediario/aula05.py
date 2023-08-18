# Dicionários

pessoa = {"nome": "joao", "idade": 25}

pessoa = dict(nome="jaum", idade=25)

pessoa["telefone"] = "3322-1235" # adiciona outra chave e valor

# Acessando dados

pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

contatos = {
    "jurandi@gmail.com":{"nome":"jaum", "telefone": "3333-2020"},
    "jurandi1@gmail.com":{"nome":"jaum2", "telefone": "3333-6666"},
    "jurandi2@gmail.com":{"nome":"jaum3", "telefone": "3333-9999", "extra":{"a":1}} # adicionando um dicionario dentro de outro
}

contatos["jurandi@gmail.com"]["telefone"]
extra = contatos["jurandi2@gmail.com"]["extra"]["a"] #selecionando o extrato
print(extra)

# Iterar
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# Metodos Dict

contatos.clear()
contatos.pop()
contatos.copy()
contatos.fromkeys() # cria chaves = quando quer criar e não vincular nenhum valor, ou criar um conjunto de chaves e com valor padrão
dict.fromkeys(["nome","telefone"], "vazio") # padrão vazio para os dois
contatos.get("chave") # se não encontrar a chave retorna None
contatos.get("chave",{}) # retorna {}
contatos.get("jurandi@gmail.com")
contatos.items()
contatos.keys() # retorna apenas as chaves

resultado = contatos.pop("jurandi@gmail.com", "nao encontrada") # valor padrão caso não seja encontrado
contatos.popitem() # exclui tudo sem precisar de chame, se não encontrado retorna erro
contatos.setdefault("nome", "jaum") # se existir ele não vai adiciomar
contatos.setdefault("idade",28) # adiciona atributo
contatos.update() # adiciona e atualiza
contatos.values() # retorna só os valores
"idade" in contatos # forma elegante de fazer uma verificação
del contatos ["jurandi1@gmail.com"]["telefone"]