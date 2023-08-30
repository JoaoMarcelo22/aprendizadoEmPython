numPedidos = int(input())
total_pedidos = """"""
pedido = 0 

def resultado():
    global total_pedidos, pedido
    for i in range(1, numPedidos + 1):
        prato = input()
        calorias = int(input())
        ehVegano = False
        pedido += 1
        if ehVegano == "s":
          ehVegano = "Vegano"
        else:
          ehVegano = "Nao-vegano"
        total_pedidos = f"Pedido {pedido} {prato}({ehVegano} - {calorias} calorias)\n"

print(total_pedidos)

resultado()