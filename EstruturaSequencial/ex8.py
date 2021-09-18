"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês."""

valorPorHora = float(input("Digite quanto você ganha por hora: R$"))
horaTrabalhada = int(
    input("Digite a quantida de horas trabalhadas nesse mês: "))

salario = horaTrabalhada * valorPorHora

print(f"No final do mês o seu salário será de: R${salario:.2f}")
