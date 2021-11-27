"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

num = float(input("Digite qualquer número, positivo ou negativo: "))

if num > 0:
    print("O valor digitado é positivo")

elif num < 0:
    print("O valor digitado é negativo")

elif num == 0:
    print("valor digitado não é positivo nem negativo")
