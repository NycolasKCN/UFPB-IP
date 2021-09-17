"""Faça um programa que solicite ao usuário a área total em metros quadrados (m2) a qual ele deseja pintar. Com essa informação, calcule a 
quantidade de latas e de galões que a loja deve fornecer para que o cliente consiga pintar no menor preço possível.
Considere que com 1 litro de tinta é possível pintar 6 metros quadrados. O Preço do galão de tinta contendo 3,6 
litros é R$ 25,00. O preço da lata de tinda contendo 18 litros é R$ 80,00.

Desenvolva três funções:

-> uma para calcular a quantidade de latas necessárias e o custo total - OK

->outra para calcular a quantidade de galões necessários e o custo total

->a terceira deverá calcular o melhor custo considerando latas e galões de tal forma a desperdiçar menos tinta.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas ou galões cheios e não 
como número fracionados."""
areaTotal = float(input("Digite o valor em metros²: "))
litroNecessarios = areaTotal / 6


def latasNecessarias():
    preço = 80.00
    litroLata = 18
    quantidadeLatas = round(litroNecessarios / litroLata + 0.5)
    custoLatas = quantidadeLatas * preço
    return quantidadeLatas, custoLatas


def galoesNecessarios():
    litroGalao = 3.6
    pass

def lataEgalao():
    pass


print(latasNecessarias())