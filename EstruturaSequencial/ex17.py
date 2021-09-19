"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1
litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
sempre arredonde os valores para cima, isto é, considere latas cheias."""
from os import system


def compraApenasLatas(litros):
    latas_necessarias = round((litros / 18) + 0.5)
    return latas_necessarias


def compraApenasGaloes(litros):
    galoes_necessarios = round((litros / 3.6) + 0.5)
    return galoes_necessarios


def compraLatasEGaloes(litros):
    litros_mais_10 = litros * (110/100)
    lata = int(litros_mais_10 / 18)
    galoes = round(((litros_mais_10 - (lata * 18)) / 3.6) + 0.5)
    return lata, galoes


system("cls")

area_pintada = float(input("Digite a o tamanho da área a ser pintada: (em M²) "))
litros_necessarios = area_pintada / 6 # 1 litro pode pintar até 6 metros quadrados

apenas_latas = compraApenasLatas(litros_necessarios)
valor_apenas_latas = apenas_latas * 80 # cada lata custa 80 reais

apenas_galoes = compraApenasGaloes(litros_necessarios)
valor_apenas_galoes = apenas_galoes * 25 # cada lata custa 25 reais

latas_e_galoes = compraLatasEGaloes(litros_necessarios)
valor_latas_e_galoes = (latas_e_galoes[0] * 80) + (latas_e_galoes[1] * 25)

print("Comprando apenas latas de 18L")
print(f"Qt. {apenas_latas} latas")
print(f"Valor R$ {valor_apenas_latas:.2f}")
print("")
print("Comprando apenas galões de 3,6L")
print(f"Qt. {apenas_galoes} galões")
print(f"Valor R$ {valor_apenas_galoes:.2f}")
print("")
print("Comprando latas de 18L e galões de 3,6L")
print("com uma folga de 10%")
print(f"Qt. {latas_e_galoes[0]} latas")
print(f"Qt. {latas_e_galoes[1]} galões")
print(f"Valor R$ {valor_latas_e_galoes:.2f}")
