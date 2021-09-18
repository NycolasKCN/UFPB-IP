"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

celsius = float(input("Digite a temperatura a ser transformada (em °C): "))

fahrenheit = ((celsius * 9) / 5) + 32

print(f"A temperatura {celsius:.1f} °C se torna {fahrenheit:.1f}")