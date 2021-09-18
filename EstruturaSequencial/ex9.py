"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius"""

fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"A temperatura em {fahrenheit} Fahrenheit se torna {celsius:.1f} em Celsius.")
