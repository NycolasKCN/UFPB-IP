"""Um belo hotel na praia tem apartamentos especialmente decorados e cobra os valores indicados na tabela a seguir. 
Com o fim do verão, o hotel resolveu oferecer 15% de desconto para hospedagens de 5 ou mais dias.
 Escreva uma função CalculaHospedagem que receba por parâmetro a quantidade de diárias e o tipo de apartamento 
 desejado, calcule e retorne o valor total a ser pago. Escreva no seu código também duas chamadas para a função, 
 passando parâmetros diferentes para cada uma delas."""

from os import system as sys

sys("cls")


# Tipo de apartamento e seus respectivos valores
dictAp = {"individual": 125,
          "suite dupla": 140,
          "suite tripla": 180}


def linha():
    print()
    print("=-" * 30)
    print()


class Checkout(object):

    def __init__(self) -> None:
        # Definir o basico sobre a hospedagem
        self.nomeCliente = ""
        self.diarias = 0
        self.tipoAp = ""

    def CauculaHospedagem(self) -> float:

        valorTipoAp = dictAp[self.tipoAp]
        valorTotalHospedagem = valorTipoAp * self.diarias

        # Conferindo quantos dias a hospedagem durou
        if self.diarias >= 5:
            return valorTotalHospedagem - (valorTotalHospedagem * 0.15)

        elif self.diarias < 5:
            return valorTotalHospedagem

    def imprimirResultado(self):
        print("{:^30}".format("CHECKOUT DE CLIENTES"))
        print("É dado 15% de desconto para o clientes")
        print("Que fiquem Hospedados por 5 dias ou mais")
        print("\n")

        print(f"O cliente: {self.nomeCliente}")
        print(f"passou {self.diarias} diarias no hotel")
        print(f"No Apartamento: {self.tipoAp}")

        valorHospedagem = self.CauculaHospedagem()
        print(f"O valor total a ser pago será de R$ {valorHospedagem:.2f}")


cliente1 = Checkout()
# pode usar uma entrada de usuario nas proximas chamadas para maior personalização
# na parte do tipo de apartamento, com um print mostrando as opções e com try e except para evitar erros
cliente1.nomeCliente = "Joselia"
cliente1.diarias = 7  # dias
cliente1.tipoAp = "individual"

cliente1.imprimirResultado()

linha()

cliente2 = Checkout()
# Como já comentado acima, pode usar um input() a seguir
cliente2.nomeCliente = "Junior"
cliente2.diarias = 2  # dias
cliente2.tipoAp = "suite tripla"

cliente2.imprimirResultado()

linha()

cliente3 = Checkout()
# Como já comentado acima, pode usar um input() a seguir
cliente3.nomeCliente = "Sinara"
cliente3.diarias = 3  # dias
cliente3.tipoAp = "suite dupla"

cliente3.imprimirResultado()
