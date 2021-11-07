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

def latasNecessarias(litrosTinta):
    preço = 80.00
    litroLata = 18
    quantidadeLatas = round((litrosTinta / litroLata) + 0.5)
    custoLatas = quantidadeLatas * preço
    return quantidadeLatas, custoLatas


def galoesNecessarios(litrosTinta):
    preço = 25.00
    litroGalao = 3.6
    quantidadeGaloes = round((litrosTinta / litroGalao) + 0.5)
    custoGalao = quantidadeGaloes * preço
    return quantidadeGaloes, custoGalao

def lataEgalao(litrosTinta):
    lata = int(litrosTinta / 18)
    execedenteLitros = ((litrosTinta / 18) - lata) * 18
    galoes = execedenteLitros / 3.6
    return lata, galoes
    

areaTotal = float(input("Digite o valor em metros²: "))
litroNecessarios = areaTotal / 6

galoes = galoesNecessarios(litroNecessarios)
latas = latasNecessarias(litroNecessarios)
latas2, galoes2 = lataEgalao(litroNecessarios)
valorMisturado = (latas2 * 80) + (galoes2 * 25)

print("-="*20)
print("Valores na lojinha do seu zé")
print("Quantidade de galões necessaria e preço: {} galões R${:.2f}".format(galoes[0], galoes[1]))
print("Quantidade de latas necessarias e preço: {} latas R${:.2f}".format(latas[0], latas[1]))
print(f" {'LATAS e GALÕES':<20}:")
print(f"R$ {valorMisturado:>15.2f}")
print(f"Qt. {latas2:>10} Lata(s)")
print(f"Qt. {latas2:>10} Galão(ões)")
print("-="*20)
