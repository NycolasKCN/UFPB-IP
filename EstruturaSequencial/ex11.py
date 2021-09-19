"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. """

numInteiro1 = int(input("Digite um número inteiro: "))
numInteiro2 = int(input("Digite outro número inteiro: "))
numReal = float(input("Digite um número real: "))

produto1 = (numInteiro1 * 2) + (numInteiro2 / 2)
soma = (3 * numInteiro1) + numReal
elevado = numReal ** 3

print(f"Este é o produto do primeiro com a metade do segundo: {numInteiro1:.1f}")
print(f"Está é a soma do triplo do primeiro com o terceiro: {soma:.1f}")
print(f"Este é o terceiro número elevado ao cubo: {elevado:.1f}")
