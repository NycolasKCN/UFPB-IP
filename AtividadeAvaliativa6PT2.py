"""Uma companhia aérea vende passagens nacionais e internacionais e cobra taxas de clientes que levem bagagens 
com peso acima do limite permitido, conforme tabela abaixo. a) Escreva uma função CalculaTaxaBagagem que receba 
por parâmetro o tipo de vôo e o peso da bagagem registrado, calcule e retorne o valor da taxa a ser paga. Escreva
duas chamadas válidas para a função."""
from os import system

system("cls")

def linha():
    print()
    print("=-" * 30)
    print()


def calculaTaxaBagagem(tipoVoo: str, pesoBagagem: float):
    """
    Imprime o tipo de voo. Caso exceda o limite de peso do tipo da viagem imprime
    um aviso e o valor da taxa a ser cobrado

    :param tipoVoo: str
    :param pesoBagagem: float
    """

    listPassagem = [
        ["nacional", 23, 6],
        ["internacional", 35, 13]
    ]

    # Passagens nacionais
    if tipoVoo == listPassagem[0][0]:
        limiteBagagem = listPassagem[0][1]
        taxaPesoExtra = listPassagem[0][2]

        print("Viagem Nacional")

        if pesoBagagem > limiteBagagem:
            pesoExtra = pesoBagagem - limiteBagagem
            valorPagar = pesoExtra * taxaPesoExtra

            print("Sua bagagem EXCEDEU o limite de peso")
            print(f"O limite era {limiteBagagem} KG e foi excedido em {pesoExtra} KG")
            print(f"A taxa cobrada será de: R$ {valorPagar:.2f}")

        elif pesoBagagem <= limiteBagagem:
            print("Sua bagagem não excedeu o limite de peso")

    # Passagens internacionais
    elif tipoVoo == listPassagem[1][0]:
        limiteBagagem = listPassagem[1][1]
        taxaPesoExtra = listPassagem[1][2]

        print("Viagem internacional")

        if pesoBagagem > limiteBagagem:
            pesoExtra = pesoBagagem - limiteBagagem
            valorPagar = pesoExtra * taxaPesoExtra

            print("Sua bagagem EXCEDEU o limite de peso")
            print(f"O limite era {limiteBagagem} KG e foi excedido em {pesoExtra} KG")
            print(f"A taxa cobrada será de: R$ {valorPagar:.2f}")

        elif pesoBagagem <= limiteBagagem:
            print("Sua bagagem não excedeu o limite de peso")

    else:
        print("Tipo de passagem não identificada. Tente novamente")


calculaTaxaBagagem("nacional", 25)

linha()

calculaTaxaBagagem("nacional", 10)

linha()

calculaTaxaBagagem("internacional", 20)

linha()

calculaTaxaBagagem("internacional", 40)


