"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

area_pintada = float(input("Digite a área a ser pintada: (em M²) "))

litros_necessarios = area_pintada / 3 # recebe a quantidade de litros a ser usados
latas_de_tinta = round((litros_necessarios / 18) + 0.5) # recebe a quantidade de latas necessarias
preco_total = latas_de_tinta * 80 # recebe o valor total da compra

print(f"Sera necessarias {latas_de_tinta} latas de tinta para pintar {area_pintada} M²")
print(f"O valor total da compra será de R$ {preco_total:.2f}")
