"""Durante a quarentena, Antenor ficou desempregado e resolveu vender Pizzas
e pastéis para poder pagar suas contas. Ele oferece sabores de pizza (por 21,50 reais cada),
e 4 sabores de pastel (5,30 reais cada). Alem disso, os clientes pagam uma taxa de entrega de R$ 1,20 por cada item
pedido. O programa abaixo deveria receber os dados do pedido de um cliente e calcular o valor final a ser pago"""

custoPizza = 21.50 # Valor fixo da pizza
custoPastel = 5.30 # Valor fixo do pastel
custoEntrega = 1.2 # Valor da entrega

qntPizza = int(input("Digite a quantidade de pizzas desejadas: "))
for pizza in range(qntPizza):
    saborPizza = input(f"Digite o sabor da {pizza + 1}ª pizza: ")

qntPastel = int(input("Digite a quantidade de pasteis desejados: "))
for pastel in range(qntPastel):
    saborPastel = input(f"Digite o sabor do {pastel + 1}º pastel: ")

# Valores do pedido
valorTotalPizza = qntPizza * custoPizza
valorTotalPastel = qntPastel * custoPastel
valorTotalEntrega = (qntPastel + qntPizza) * custoEntrega

valorAPagar = valorTotalPastel + valorTotalPizza + valorTotalEntrega
print("O valor total a ser pago é R$: {:.2f}".format(valorAPagar))

