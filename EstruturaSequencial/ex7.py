"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

lado = float(input("Digite o valor em centimetros de um lado do quadrado: "))

area = lado ** 2
dobroArea = area * 2

print(f"O dobro da área digitada é {dobroArea:.1f} cm")
