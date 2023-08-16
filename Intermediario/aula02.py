# metodos de classe list

lista = []

lista.append(1) # Adiciona
lista.clear() # Limpa a lista
l2 = lista.copy() # Faz uma copia da lista, mas o que se faz em lista não reflete em L1
lista.count(1) # retorna quantas unidades do objeto foram encontrados
lista.extend(["java", "csharp"]) # junta uma lista a outra
lista.index("java") # retorna a primeiro ocorrencia index onde o objeto for encontrado
lista.pop() # exclui o ultimo elemento adicionado OU via index declarado
lista.remove("java") # exclui um objeto em destaque tira apenas a primeira ocorrencia
lista.reverse() # inverte a ordem dos itens na lista 
lista.sort() # odernagem padrão
lista.sort(reverse=True) # ordena de traz para frente
lista.sort(key=lambda x: len(x)) # ordem crescente referente ao tamanho do objeto "Lambda é uma função anonima"
lista.sort(key=lambda x: len(x), reverse=True) # altera a ordem 
len(lista) # pega o tamanho total da lista
sorted(lista, key=lambda x: len(x)) #função
sorted(lista, key=lambda x: len(x), reverse=True) #função

